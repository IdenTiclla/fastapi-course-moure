from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_default_route():
    return {"hello": "world"}

@app.get("/url")
def get_url_course():
    return {"url": "http://some-url.com"}