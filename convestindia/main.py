# FastAPI Libraries
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# Broker Libraries (Alice Blue)
from pya3 import *

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# class Authenticate(BaseModel):
#     user_id: str
#     api_key: str

names = ["ashish", "ashu", "arish", "ashwan", "anish","avash,","ankine", "anveshak", "arish"]

@app.get("/", response_class=HTMLResponse)
async def index(request: Request): # get request for Order Control page
    return templates.TemplateResponse(
        "display.html", {"request": request, 
                         "login_status": ""
                         "names": names}
    )


@app.post("/", response_class=HTMLResponse)
async def index_post(
    request: Request, 
    user_id: str = Form(...),
    api_key: str = Form(...),
    search: str = Form(...)
    ):
    try:
        # generate api key in https://ant.aliceblueonline.com/apps 
        alice = Aliceblue(user_id=user_id, api_key=api_key)
        session = alice.get_session_id() # Get Session ID
        if 'sessionID' in session:
            login_status = "Successfully Logged In"
        elif session['emsg'] == "API key not available. Please generate API key":
            login_status = "Invalid API Key. Please regenerate or enter a valid API Key."
        else:
            login_status = session["emsg"]  
            
            
            
            
            
        return templates.TemplateResponse(
            "display.html", {"request": request, 
                             "login_status": str(login_status)
                             "names": names, 
                             "selected": search}
        )
        
    except Exception as e:
        return templates.TemplateResponse(
            "display.html", {"request": request, 
                             "login_status": str(e),
                             "names": names, 
                             "selected": search}
        )



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
