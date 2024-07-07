from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit_name")
async def submit_name(request: Request, name: str = Form(...)):
    valid_names = {"ashish": "bangalore", "anish": "hyderabad"}
    if name.lower() in valid_names:
        return templates.TemplateResponse("index.html", {"request": request, "show_place_form": True, "name": name})
    else:
        return templates.TemplateResponse("index.html", {"request": request, "error": "Wrong name"})

@app.post("/submit_place")
async def submit_place(request: Request, name: str = Form(...), place: str = Form(...)):
    if name.lower() in valid_names and place.lower() == valid_names[name.lower()]:
        return templates.TemplateResponse("index.html", {"request": request, "success": f"Correct! {name.capitalize()} is from {place.capitalize()}."})
    else:
        return templates.TemplateResponse("index.html", {"request": request, "error": "Wrong place", "show_place_form": True, "name": name})
    
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.4", port=8000)