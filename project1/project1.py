from fastapi import Request, APIRouter


Project1Router = APIRouter(prefix="/api/v1")

@Project1Router.post("/project1_data")
async def get_p1_data(req: Request):
    try:
        data = await req.json()
        print(f"project1 data: {data}")
        return {"status": "success", "data": data}


    except Exception as e:
        print(f"An Error occured on our site project1 {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))