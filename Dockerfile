FROM python:3.8.10

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD python main.py