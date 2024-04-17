FROM continuumio/miniconda3
    
WORKDIR /home/app

RUN pip install streamlit pandas plotly

COPY . /home/app/

CMD streamlit run --server.port 8501 test.py
