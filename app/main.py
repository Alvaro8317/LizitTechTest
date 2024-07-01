from fastapi import FastAPI
from routers import item_router

app = FastAPI()
app.title = 'LizitTechTest'
app.version = '0.0.1'
app.include_router(item_router)
