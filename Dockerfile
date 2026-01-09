FROM python:3.11-slim

RUN apt-get update && apt-get install -y ffmpeg && pip install --no-cache-dir aiogram yt-dlp python-dotenv

WORKDIR /app

COPY . /app

RUN mkdir -p videos

CMD ["python", "bot.py"]