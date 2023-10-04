FROM python:3.8-slim

WORKDIR /sqlcron

COPY env.txt .

RUN pip install -r env.txt

COPY . .

CMD ["python","SQLscript.py"]
