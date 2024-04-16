FROM python:3.8

WORKDIR /home/app

# RUN apt-get update
# RUN apt-get install nano unzip
RUN apt install curl -y

RUN curl -fsSL https://get.deta.dev/cli.sh | sh
RUN pip install boto3 pandas numpy gunicorn streamlit scikit-learn matplotlib seaborn plotly xgboost
COPY . /home/app

CMD streamlit run --server.port 8501 app.py