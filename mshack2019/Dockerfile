FROM python:3.6

WORKDIR /app

ADD . /app

RUN pip3 install Cython --install-option="--no-cython-compile"

RUN pip3 install fasttext

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

RUN pip3 install nltk

RUN [ "python", "-c", "import nltk; nltk.download('punkt');" ]

#EXPOSE 5001

#CMD ["python3", "app.py"]

