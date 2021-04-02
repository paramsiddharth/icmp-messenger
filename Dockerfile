# A Python 3.8-slim image
FROM python:3.8-slim

# Copy files to container
WORKDIR /app
ADD . /app

# Install dependencies
RUN pip install -r requirements.txt

ENTRYPOINT ["./run.sh"]
CMD ["./run.sh"]