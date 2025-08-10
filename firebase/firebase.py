from fastapi import APIRouter
from logger import logger
from firebase.config import auth


FirebaseRouter = APIRouter(prefix="/api/v1")


required_fields = ["email","password"]

@FirebaseRouter.post("/create_user")
async def create_user(payload: dict):
    for req in required_fields:
        if not payload.get(req):
            return {"error":f"Field '{req}' is required"}
    try:
        auth.create_user(
            email=payload["email"],
            password=payload["password"]
        )
        await logger.info("User created Successfully",extra={"payload": payload})
        return {"message":"User Created Successfully"}
    except Exception as e:
        await logger.error("Firebase Auth connection failed",e)

