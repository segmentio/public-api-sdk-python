FROM python:latest

COPY . /papi-python-sdk
WORKDIR /papi-python-sdk

# Install runtime dependencies
RUN pip3 install -r requirements.txt
RUN pip3 install -r ut-requirements.txt
RUN pip3 install tox
