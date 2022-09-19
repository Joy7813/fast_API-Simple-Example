from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import templates

app= FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/login')     
def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request}) 