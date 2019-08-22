FROM ubuntu:18.04

# Set timezone to America/Chicago
ENV TZ=America/Chicago
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Update and install dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    software-properties-common \
    nano \
    git \
    build-essential \
    python3.7 \
    python3.7-dev \
    python3-pip \
    libmysqlclient-dev

RUN python3 -m pip install pip --upgrade

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_READ_DOT_ENV_FILE 1

# Create and set work directory
RUN mkdir -p /opt/amethyst
WORKDIR /opt/amethyst

# Copy project code
COPY . /opt/amethyst

# Install dependencies
RUN pip3 install -r requirements.txt

# Collectstatic
RUN python3 /opt/amethyst/application/manage.py collectstatic

# Expose port 8000 for traffic
EXPOSE 8000

# Default container startup command
CMD [ "/opt/amethyst/start.sh" ]
