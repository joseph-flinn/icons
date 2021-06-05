from fastapi import FastAPI

from .icon_parser import parse_icon

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/{hostname}/icon.png")
def get_icon(hostname: str) -> dict:
    return {
        "hostname": hostname,
        "icons": parse_icon(hostname)
    }
