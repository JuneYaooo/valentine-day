FROM june666666/valentine_env:valentine_20230213

WORKDIR /code
COPY ./tmp/code/*.py /code/
COPY ./tmp/code/*.mp4 /code/

RUN apt-get update && rm -rf /var/lib/apt/lists/*
EXPOSE 8501

CMD ["bash", "-c", "source activate valentine && streamlit run run.py"]

