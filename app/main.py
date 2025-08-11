# reconmaster/app/main.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .db import models
from .db.database import engine
from .api import routes

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ReconMaster API",
    description="An API for running reconnaissance tools.",
    version="0.1.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(routes.router, prefix="/api")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    """
    Serves the main index.html page.
    """
    return templates.TemplateResponse("index.html", {"request": request})

# --- NEW: Route to serve the history page ---
@app.get("/history", response_class=HTMLResponse)
def read_history(request: Request):
    """
    Serves the history.html page.
    """
    return templates.TemplateResponse("history.html", {"request": request})
