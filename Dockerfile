FROM python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /efollowup-googlesheets
ADD . /efollowup-googlesheets

RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirements.txt

CMD ["python","app.py"]