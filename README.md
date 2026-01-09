# VKVideoDownloader

Простой Telegram-бот, который позволяет скачивать видео из VK по ссылке и присылает их прямо в Telegram.  
Работает через aiogram 3** и yt-dlp, полностью готов к запуску в Docker.

---

## ⚡ Функции

- Скачивание публичных VK (приватные видео не работают)
- Поддержка файлов больших размеров (через `sendDocument`)  
- При запуске программы, удали папку cookies.txt
- Docker + docker-compose для быстрого запуска 24/7  
- Автоматический выбор `sendVideo` или `sendDocument` в зависимости от размера файла

---

## Требования

- Python 3.11+  
- Docker + Docker Compose  
- ffmpeg (устанавливается в Docker автоматически)  
- Токен Telegram бота (через @BotFather)
- Мой телеграм бот: @vkvidloader_bot

---

## 🛠 Установка и запуск

1. Клонируем репозиторий:

```bash
git clone https://github.com/YourUsername/VKVideoDownloader.git
cd VKVideoDownloader
