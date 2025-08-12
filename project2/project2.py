from fastapi import Request, APIRouter,HTTPException

Project2Router = APIRouter(prefix="/api/v1")

@Project2Router.post("/project2_data")
async def get_p2_data(req: Request):
    try:
        data = await req.json()
        print(f"project2 data: {data}")
        return {"status": "success", "data": data}

    except Exception as e:
        print(f"An Error occured on our site project2 {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))