FROM python:3.6-alpine as base

FROM base as builder

RUN mkdir /packages
WORKDIR /packages

COPY requirements.txt /requirements.txt

# Install application dependencies
RUN pip install --install-option="--prefix=/packages" -r /requirements.txt

FROM base

# Create User
RUN addgroup -S app && adduser -S -G app app

COPY --from=builder /packages /home/app/.local/
USER app

# Copy Data In For Setup
COPY . /code/

WORKDIR /code

CMD ["python", "consumer.py"]
