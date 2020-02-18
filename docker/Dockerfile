FROM python:3.7-alpine

MAINTAINER xw.hu <xw.hu@tianrang-inc.com>

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com && rm -rf /tmp/*

RUN echo "net.core.somaxconn=65535" >> /etc/sysctl.conf

COPY src /mysite/src
COPY static /mysite/static
COPY templates /mysite/templates
COPY app.py /mysite/app.py

WORKDIR /mysite

ENV TZ=Asia/Shanghai

CMD ["python3", "app.py"]
