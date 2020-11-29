FROM debian

RUN apt-get update && apt-get install -y apache2 \
    libapache2-mod-wsgi-py3 \
    build-essential \
    python3 \
    python3-dev\
    python3-pip \
    python3-flask \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

COPY ./URL_SHORTENER/ /var/www/html/URL_SHORTENER
RUN pip3 install virtualenv

COPY ./url_shortener.conf /etc/apache2/sites-available/url_shortener.conf
RUN ln -s /etc/apache2/sites-available/url_shortener.conf /etc/apache2/sites-enabled/url_shortener.conf
RUN a2enmod headers
# Disbaling the default apache page
RUN a2dissite 000-default

# LINK apache config to docker logs.
RUN ln -sf /proc/self/fd/1 /var/log/apache2/access.log && \
    ln -sf /proc/self/fd/1 /var/log/apache2/error.log


# Set up virtualenv
RUN python3 -m virtualenv /var/www/html/URL_SHORTENER/venv && \
    . /var/www/html/URL_SHORTENER/venv/bin/activate && \
    pip install -r /var/www/html/URL_SHORTENER/requirements.txt

EXPOSE 80

WORKDIR /var/www/html/URL_SHORTENER

CMD  /usr/sbin/apache2ctl -D FOREGROUND
