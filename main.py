from fastapi import HTTPException,status,FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
app = FastAPI()
from logger import logger

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,          
    allow_methods=["*"],    
    allow_headers=["*"],
)

@app.get("/")
async def ping():
    logger.info("Hello from server")
    print("server is on")

if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)

