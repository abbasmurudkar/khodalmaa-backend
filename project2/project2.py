from fastapi import APIRouter,HTTPException
from logger import logger
from firebase.config import auth


Project2Router = APIRouter(prefix="/api/v1")



