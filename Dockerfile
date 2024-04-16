FROM python:3.10-slim
WORKDIR /app
RUN pip install --no-cache-dir cohere


# docker run -v C:\Users\loico\Documents\glossy:/app:z -it connortbot/personal-py:glossy-env