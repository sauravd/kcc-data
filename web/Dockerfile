FROM python:3.11-slim

# Install netcat-openbsd and gettext for makemessages
RUN apt-get update \
&& apt-get install -y --no-install-recommends \
      netcat-openbsd \
      gettext \
&& rm -rf /var/lib/apt/lists/*

WORKDIR /code


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .
