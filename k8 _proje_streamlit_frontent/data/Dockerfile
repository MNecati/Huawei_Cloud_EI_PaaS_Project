FROM python:3.7
COPY . /data
WORKDIR /data
EXPOSE 80
RUN pip install -r requirements.txt
CMD streamlit run main.py --server.port 80
