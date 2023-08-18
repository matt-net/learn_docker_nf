FROM python:3.10-slim

# set the working directory in the container
WORKDIR /code

# copy requirements files
COPY requirements.txt ./

# update pip
RUN python -m pip install --upgrade pip

# install dependencies
RUN pip install -r requirements.txt

# copy the dependencies file to the working directory
COPY . .

# run the command
ENTRYPOINT ["python", "main.py"]