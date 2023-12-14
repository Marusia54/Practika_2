from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from public.users import users_router

app = FastAPI()

app.include_router(users_router)


@app.get("/", response_class=PlainTextResponse)
def root_page():
    return "Добро пожаловать!"
