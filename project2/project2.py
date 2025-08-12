from fastapi import Request, APIRouter

Project2Router = APIRouter(prefix="/api/v1")

@Project2Router.post("/project2_data")
async def get_p2_data(req: Request):
    try:
        data = await req.json()
        print(f"project2 data: {data}")
        return {"status": "success", "data": data}

    except Exception as e:
        print(f"Error in get_p2_data: {str(e)}")
        return {"status": "error", "message": str(e)}