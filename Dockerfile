FROM openfaas/classic-watchdog:0.18.1 as watchdog

FROM python:3-alpine
ARG ADDITIONAL_PACKAGE
COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog
RUN apk --no-cache add ca-certificates ${ADDITIONAL_PACKAGE}
RUN addgroup -S app && adduser app -S -G app
WORKDIR /home/app/
COPY run.py           .
COPY verifier.py       .
COPY requirements.txt .
RUN chown -R app /home/app &&   mkdir -p /home/app/python && chown -R app /home/app
USER app
ENV PATH=$PATH:/home/app/.local/bin:/home/app/python/bin/
ENV PYTHONPATH=$PYTHONPATH:/home/app/python
RUN pip install -r requirements.txt --target=/home/app/python
WORKDIR /home/app/
USER root
RUN chown -R app:app ./ &&   chmod -R 777 /home/app/python
USER app
ENV APP_USER app
ENV APP_UID 9999
ENV APP_GID 9999
RUN addgroup -S -g $APP_GID $APP_USER  \
    && adduser -S -u $APP_UID -G $APP_USER $APP_USER

USER $APP_UID
ENV fprocess="python3 run.py" content_type="application/json"
EXPOSE 8080
HEALTHCHECK --interval=3s CMD [ -e /tmp/.lock ] || exit 1
CMD ["fwatchdog"]
