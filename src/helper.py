import pandas as pd
import joblib
import yaml
import io
import os
from tqdm import tqdm
import gdown
# google API
# from google.oauth2 import service_account
# from googleapiclient.discovery import build
# from googleapiclient.http import MediaIoBaseDownload
# from googleapiclient.errors import HttpError
# Preprocessing Data
from sklearn.preprocessing import OneHotEncoder
# model
import xgboost as XGB
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import f1_score, recall_score, precision_score

def save_to_pickle(data, file_path):
    # Extract the directory from the file path
    directory = os.path.dirname(file_path)

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save the data to a pickle file using joblib
    joblib.dump(data, file_path)

def load_params(param_dir):
    print("loading configuration file....")
    try:
        with open(param_dir, 'r') as file:
            params = yaml.safe_load(file)
            print("Configuration file loaded")
            return params
    except FileNotFoundError as fe:
        raise RuntimeError("Parameters file not found in the specified path.")


def download_file_to_dataframe(file_id):
    # Temporary file path
    temp_filepath = "temp_data.csv"

    gdown.download(f"https://drive.google.com/uc?id={file_id}", temp_filepath, quiet=False)

    # Load the content of the file into a DataFrame
    df = pd.read_csv(temp_filepath)

    # Clean up the temporary file
    os.remove(temp_filepath)

    return df

def extractInputOutput(data,
                       output_column_name,
                       column_to_drop):
        data = data.drop(columns=column_to_drop)
        output_data = data[output_column_name]
        input_data = data.drop(output_column_name, axis=1)

        return input_data, output_data 
      
def splitNumCat(data):
    list_num = [var for var in data.columns if data[var].dtype != 'O']
    list_object = [var for var in data.columns if data[var].dtype == 'O']
    print("succes split numeric categoric column")
    return list_num, list_object



def onehot( data, col_cat, col_num, encoder_col=None, encoder=None):
    if encoder_col is None:
        encoder_col = {col: data[col].unique() for col in col_cat}
    
    if encoder is None:
        encoder = OneHotEncoder(categories=[encoder_col[col] for col in col_cat], sparse=False)
        encoder.fit(data[col_cat])
    else:
        encoder.categories_ = [encoder_col[col] for col in col_cat]

    X_train_cat_ohe = encoder.transform(data[col_cat])
    ohe_col = encoder.get_feature_names_out(col_cat)

    X_train_cat_ohe = pd.DataFrame(X_train_cat_ohe, columns=ohe_col, index=data.index)
    data_numeric_ohe = pd.concat([data[col_num], X_train_cat_ohe], axis=1)
    print("OneHotEncoder succeeded")
    return data_numeric_ohe

def create_param_grid():
    param_grid = [
        {
            'subsample': [0.9, 0.8],
            'n_estimators': [900, 500],
            'max_depth': [6, 9],
            'learning_rate': [0.1],
            'colsample_bytree': [0.8, 0.9]
        }
    ]
    return param_grid

def fit_model(param_grid, xtrain, ytrain, xval, yval, xtest, ytest):
    xgb_model = XGB.XGBClassifier()
    with tqdm(total=len(param_grid), desc="Randomized Search") as pbar:
        random_search = RandomizedSearchCV(
            estimator=xgb_model,
            param_distributions=param_grid[0],  # Access the first dictionary in the list
            n_iter=1,  # Each dictionary is a single configuration
            scoring='f1_macro',
            cv=5,
            verbose=1,
            n_jobs=-1
        )

        random_search.fit(xtrain, ytrain)
        pbar.update(1)

        print("Best parameters found:", random_search.best_params_)
        print("fit to data val")
        xgb_model_final = XGB.XGBClassifier(**random_search.best_params_)
    
        xgb_model_final.fit(xtrain, ytrain)
        y_pred_val_xgb = xgb_model_final.predict(xval)
        f1 = f1_score(yval, y_pred_val_xgb)
        recall = recall_score(yval, y_pred_val_xgb)
        precision = precision_score(yval, y_pred_val_xgb)
        print("F1-score: ", f1)
        print("recall: ", recall)
        print("precision: ", precision)

        print("#####" * 3, "fit to test", "#####" * 3)
        
        y_pred_test_xgb = xgb_model_final.predict(xtest)
        f1 = f1_score(ytest, y_pred_test_xgb)
        recall = recall_score(ytest, y_pred_test_xgb)
        precision = precision_score(ytest, y_pred_test_xgb)
        print("F1-score: ", f1)
        print("recall: ", recall)
        print("precision: ", precision)
        config = load_params("config.yaml")
        save_to_pickle(xgb_model_final, config['XGBoost_model'][2])
        print("Save to pickle")
       