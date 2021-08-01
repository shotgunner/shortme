FROM python:3.7.7
ADD ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . /srv
WORKDIR /srv
RUN python migrate.py
CMD python app.py