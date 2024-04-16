FROM python:3.8

WORKDIR /home/app

RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libc-dev \
    # Ajoutez d'autres dépendances ici si nécessaire \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && apt-get install -y nano unzip curl

RUN pip install boto3 pandas joblib gunicorn streamlit pydeck scikit-learn hdbscan matplotlib xgboost seaborn 

COPY . /home/app

# Exécutez l'application Streamlit sur le port 4000
CMD ["streamlit", "run", "--server.port", "4000", "home.py"]
