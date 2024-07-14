from fastapi import FastAPI
from routers import users
app = FastAPI()

# Configuring routers
app.include_router(users.router)

@app.get("/")
def get_default_route():
    return {"hello": "world"}

@app.get("/url")
def get_url_course():
    return {"url": "http://some-url.com"}