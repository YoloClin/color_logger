FROM python:3.7
# Based on pycommon v0.5

RUN pip3 install --no-cache-dir \
        pylint anybadge pytest coverage pytest-cov mypy

WORKDIR /app

ENTRYPOINT ["sh", ".ci/run-tests.sh"]
