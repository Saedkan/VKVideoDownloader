import asyncio
import os
import subprocess
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from aiogram.types import FSInputFile

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

DOWNLOAD_DIR = "videos"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "Привет!\n"
        "Отправь ссылку на видео из VK - я скачаю и пришлю тебе файл."
    )

@dp.message()
async def download_vk_video(message: types.Message):
    url = message.text.strip()

    if "vk.com" not in url:
        await message.answer("Отправь корректную ссылку на видео из VK")
        return

    await message.answer("Скачиваю видео...")

    output_template = os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s")

    command = [
        "yt-dlp",
        "-f", "best",
        "-o", output_template,
        url
    ]

    cookies_path = "cookies.txt"
    if os.path.isfile(cookies_path) and os.path.getsize(cookies_path) > 0:
        command.insert(1, "--cookies")
        command.insert(2, "cookies.txt")

    try:
        subprocess.run(command, check=True)

        files = os.listdir(DOWNLOAD_DIR)
        if not files:
            await message.answer("Не удалось найти скачанное видео")
            return

        filepath = os.path.join(DOWNLOAD_DIR, files[0])

        if os.path.getsize(filepath) > 50*1024*1024:
            await message.answer_document(document=FSInputFile(filepath), caption="Готово!")
        else:
            await message.answer_video(video=FSInputFile(filepath), caption="Готово!")

        video = FSInputFile(filepath)

        await message.answer_video(
            video=video,
            caption="Готово!",
            timeout=300
        )

        await message.answer_document(
            document=video,
            caption="Готово!"
        )

    except subprocess.CalledProcessError:
        await message.answer("Ошибка при загрузке видео")
    finally:
        for f in os.listdir(DOWNLOAD_DIR):
            os.remove(os.path.join(DOWNLOAD_DIR, f))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())