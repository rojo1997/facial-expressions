FROM python:3.6 as facial-expressions

COPY requirements.txt /facial-expressions/

WORKDIR /facial-expressions

RUN apt-get update && \
    apt-get install -y ffmpeg libsm6 libxext6 && \
    apt-get clean && \
    python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir -r requirements.txt

COPY . /facial-expressions

USER daemon

EXPOSE 5030
CMD [ "python", "-u", "app/main.py" ]