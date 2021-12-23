FROM python:3-slim AS build-env
COPY ./main.py /app/main.py
WORKDIR /app


FROM gcr.io/distroless/python3
MAINTAINER einfachnuralex
LABEL org.opencontainers.image.source https://github.com/einfachnuralex/echo-udp

COPY --from=build-env /app /app
WORKDIR /app
CMD ["main.py"]