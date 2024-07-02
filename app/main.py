from fastapi import FastAPI
from routers import item_router
from config.database import Base, engine
from middlewares.error_handler import ErrorHandlerMiddleware

app = FastAPI()
app.title = 'LizitTechTest'
app.version = '0.0.1'
app.add_middleware(ErrorHandlerMiddleware)
Base.metadata.create_all(bind=engine)
app.include_router(item_router)
