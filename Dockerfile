FROM python:3.6-slim-stretch

RUN apt update && \
    apt install -y python3-dev gcc

ADD . /crop-plant

WORKDIR /crop-plant

# Install pytorch and fastai
#RUN pip install torch_nightly -f https://download.pytorch.org/whl/nightly/cpu/torch_nightly.html



RUN pip install -r requirements.txt

CMD python manage.py runserver
