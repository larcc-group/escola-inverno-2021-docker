FROM python:3.9.6

RUN pip install --no-cache-dir matplotlib==3.4.2

RUN mkdir /home/data
COPY average-attendance.py /home
COPY data /home/data

WORKDIR /home

CMD [ "python", "average-attendance.py" ]
