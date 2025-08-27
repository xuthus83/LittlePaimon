FROM docker.1ms.run/python:3.9-slim-bullseye

RUN pip3 install --no-cache-dir --default-timeout=1000 nb-cli -i https://pypi.doubanio.com/simple

ENV TZ=Asia/Shanghai \
    DEBIAN_FRONTEND=noninteractive

RUN ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime && \
    echo ${TZ} > /etc/timezone && \
    dpkg-reconfigure --frontend noninteractive tzdata

RUN apt-get update && apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /data/pkg

COPY . .

RUN sed -i 's/^\-\-index\-url\s.*$//' requirements.txt && \
    pip3 install --no-cache-dir --default-timeout=60 -r requirements.txt -i https://pypi.doubanio.com/simple

RUN playwright install-deps && \
    playwright install chromium && \
    rm -rf /var/lib/apt/lists/*

CMD ["nb", "run"]