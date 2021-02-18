# Base alpine image
FROM python:3.7.9-alpine3.13

# Install java 8 
RUN apk update \
&& apk upgrade \
&& apk add --no-cache build-base \
&& apk add --no-cache bash \
&& apk add --no-cache --virtual=build-dependencies unzip \
&& apk add --no-cache curl \
&& apk add --no-cache openjdk8-jre

# Set the java path
ENV JAVA_HOME="/usr/lib/jvm/java-1.8-openjdk"

# Create directory
RUN mkdir /etc/invoice_digitizer

# Define working directory
WORKDIR /etc/invoice_digitizer

# Install app dependencies
COPY requirements.txt ./

# Install requirements
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Copy the files into the directory
COPY ./ /etc/invoice_digitizer

CMD ["python", "run.py"]

EXPOSE 5000