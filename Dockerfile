FROM python

WORKDIR /programa

RUN pip install numpy

COPY . .

CMD ["python","main.py"]