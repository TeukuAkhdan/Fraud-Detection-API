import pandas as pd
import yaml
import helper
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, recall_score, precision_score, accuracy_score, f1_score
import xgboost as xgb

params = helper.load_params("config.yaml")

# Pre-paration
fileid='1c7laYddFFeOR1PmC-V3fT1SOqRe32S5W'
data = helper.download_file_to_dataframe(fileid)
X, Y = helper.extractInputOutput(data, params['output_column_name'][0].strip(), params['list_drop_column'])

# split data
X_train, X_temp, Y_train, Y_temp = train_test_split(X, Y, test_size=0.3, random_state=42)
X_val, X_test, Y_val, Y_test = train_test_split(X_temp, Y_temp, test_size=0.5, random_state=42)

# Preprocessing Data
list_num, list_object = helper.splitNumCat(X_train)
encoder_col = {col: X_train[col].unique() for col in list_object}
X_train = helper.onehot(data=X_train, col_cat=list_object, col_num=list_num, encoder_col=encoder_col)
X_val = helper.onehot(data=X_val, col_cat=list_object, col_num=list_num, encoder_col=encoder_col)
X_test = helper.onehot(data=X_test, col_cat=list_object, col_num=list_num, encoder_col= encoder_col)

# fit model
param = helper.create_param_grid()
helper.fit_model(param_grid=param, 
                          xtrain= X_train,
                          ytrain = Y_train,
                          xval = X_val,
                          yval = Y_val,
                          xtest = X_test,
                          ytest = Y_test 
                          )
