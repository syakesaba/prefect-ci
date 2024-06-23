FROM prefecthq/prefect:2.19.5-python3.11
COPY ./requirements.txt .
RUN python -m pip install -r requirements.txt --trusted-host pypi.python.org --no-cache-dir
COPY . /opt/prefect/
WORKDIR /opt/prefect/