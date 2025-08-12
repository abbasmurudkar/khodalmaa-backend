from fastapi import Request, APIRouter
import os

Project1Router = APIRouter(prefix="/api/v1")

@Project1Router.post("/project1_data")
async def get_p1_data(req: Request):
    try:
        data = await req.json()
        print(f"project1 data: {data}")
        return {"status": "success", "data": data}

    except Exception as e:
        # Log error (optional: replace with actual logger)
        print(f"Error in get_p1_data: {str(e)}")
        return {"status": "error", "message": str(e)}