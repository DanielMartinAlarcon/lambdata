FROM debian

### *Minimal* Python container
### So logging/io works reliably w/Docker
ENV PYTHONUNBUFFERED=1

### Basic Python dev dependencies
RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install python3-pip curl nano -y && \
  pip3 install pandas && \
  pip3 install sklearn && \
  pip3 install seaborn && \
  pip3 install -i https://test.pypi.org/simple/ lambdata-danielmartinalarcon && \
  python3 -c "import lambdata_danielmartinalarcon; print('Success!')"
