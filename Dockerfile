FROM continuumio/miniconda3
    
WORKDIR /home/app

RUN pip install streamlit pandas numpy plotly seaborn

COPY . /home/app/

CMD streamlit run --server.port 8501 test.py

# #COPY requirements.txt /dependencies/requirements.txt
# RUN pip install -r /dependencies/requirements.txt