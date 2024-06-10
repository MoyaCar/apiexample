FROM python:3.12
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
CMD ["fastapi", "run", "main.py", "--port", "80"]