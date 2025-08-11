from fastapi import FastAPI, Request,HTTPException,APIRouter
import httpx
import asyncio
from fastapi.middleware.cors import CORSMiddleware
from logger import logger
import os

TelegramRouter = APIRouter(prefix="/api/v1")


bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")  # e.g., 123456789

@TelegramRouter.post("/send-alert")
async def send_telegram_alert(req: Request):
    data = await req.json()
    message = data.get("message", "No message received")

    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(telegram_url, json=payload)
        return {"telegram_response": response.json()}