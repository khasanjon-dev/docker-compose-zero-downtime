FROM python:3.10.6-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app
ADD /backend /app/backend
ADD /devops/backend /app/devops/backend

RUN apt-get update && \
    apt-get install -y netcat
RUN pip install --upgrade pip
RUN #pip install -r /app/backend/requirements.txt --no-cache-dir
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r /app/backend/requirements.txt

ENTRYPOINT [ "/app/devops/backend/entrypoint.sh" ]