# start by pulling the python image
FROM python:3.8


# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file\
RUN apt-get update && apt-get install -y python3-dev gcc libc-dev libffi-dev
RUN pip install flask
RUN pip install -r requirements.txt
#RUN apk add --no-cache --virtual .build-deps gcc libffi-dev musl-dev && pip install cython \
# && pip install cffi && apk del .build-deps gcc libffi-dev musl-dev && pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
EXPOSE 5000  
CMD [ "python3","rmm/index.py" ]

