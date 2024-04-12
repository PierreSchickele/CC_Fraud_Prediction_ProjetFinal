FROM continuumio/miniconda3
    
WORKDIR /home/app

RUN pip install streamlit pandas numpy plotly seaborn

COPY . /home/app/

CMD streamlit run --server.port $PORT test.py