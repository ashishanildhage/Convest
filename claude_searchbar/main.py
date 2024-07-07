from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

names = ["ashish", "ashu", "arish", "ashwan", "anish","avash,","ankine", "anveshak", "arish"]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "names": names})

@app.post("/", response_class=HTMLResponse)
async def submit(request: Request, search: str = Form(...)):
    return templates.TemplateResponse("index.html", {"request": request, "names": names, "selected": search})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.3", port=8000)
