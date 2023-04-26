# FROM python:3.9

# WORKDIR /app
# RUN apt-get update
# RUN apt-get install libsm6 libxext6 tesseract-ocr tesseract-ocr-spa  -y

# ENV TZ America/Mexico_City

# RUN apt-get -y update
# RUN apt-get install -y libzbar0
# RUN apt-get install -y --fix-missing \
#     build-essential \
#     cmake \
#     gfortran \
#     git \
#     wget \
#     curl \
#     graphicsmagick \
#     libgraphicsmagick1-dev \
#     libatlas-base-dev \
#     libavcodec-dev \
#     libavformat-dev \
#     libgtk2.0-dev \
#     libjpeg-dev \
#     liblapack-dev \
#     libswscale-dev \
#     pkg-config \
#     python3-dev \
#     python3-numpy \
#     software-properties-common \
#     zip \
#     && apt-get clean && rm -rf /tmp/* /var/tmp/*


# RUN cd ~ && \
#     mkdir -p dlib && \
#     git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ && \
#     cd  dlib/ && \
#     python3 setup.py install --yes USE_AVX_INSTRUCTIONS



# RUN apt-get install -y libsndfile-dev 
# RUN pip install imutils
# RUN pip install redis

# COPY . .
# RUN cd ~
# RUN pip install --upgrade pip && pip install --no-cache-dir -r /app/requirimientos.txt

# EXPOSE 3000

# CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "3000"]

# CMD ["python", "manage.py", "runserver", "0.0.0.0:3000"]

FROM franciscolopez29/preface:all

WORKDIR /app
COPY . .

RUN cd ~

RUN apt-get install -y libsndfile-dev

RUN pip install imutils
RUN pip install redis

EXPOSE 3000

CMD ["sh", "entrypoint.sh"]