# FROM python:3.9.0-slim-buster

# WORKDIR /home

# COPY requirement.txt ./
# COPY src/helper.py src/training.py src/main.py src/app.py config/config.yaml Data/project-auth-409416-0c17d95f33b3.json ./

# RUN pip install -r requirement.txt

# EXPOSE 8000 8501

# # Train the ML model
# RUN python training.py

# # CMD to run FastAPI and Streamlit
# CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 & streamlit run --server.port 8501 app.py"]



FROM python:3.10.2-slim-buster

WORKDIR /home

COPY requirement.txt ./
COPY src/helper.py src/training.py src/main.py src/app.py config/config.yaml ./
COPY models/tuning/XGB_model_final.pkl /home/models/tuning/

RUN pip install -r requirement.txt

EXPOSE 8000 8501

# CMD to run FastAPI and Streamlit with training
# CMD ["sh", "-c", "python training.py && uvicorn main:app --host 0.0.0.0 --port 8000 --reload & streamlit run --server.port 8501 app.py"]
# CMD to run FastAPI and Streamlit Without training
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 --reload & streamlit run --server.port 8501 app.py"]
