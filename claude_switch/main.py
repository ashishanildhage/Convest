from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

    
@app.get("/toggle", response_class=HTMLResponse)
async def read_item(request: Request):
    """Returns the initial state of the slider.

    This function is used to provide the initial state of the slider on the
    front-end. It's also used as the fallback when the slider is reset.

    Args:
        request (Request): The request object.

    Returns:
        TemplateResponse: The HTML template with the initial slider state.
    """
    return templates.TemplateResponse(
        "index.html", {"request": request, "state": "left", "action": "Buy"}
    )



@app.post("/toggle", response_class=HTMLResponse)
async def toggle(request: Request, state: str = Form(...)):
    """
    Toggle the action between 'Buy' and 'Sell' based on the state.

    Args:
        request (Request): The request object.
        state (str): The current state of the slider ('left' or 'right').

    Returns:
        TemplateResponse: The HTML template with the updated slider state and action.
    """
    # Toggle the action between 'Buy' and 'Sell' based on the state
    action = "Sell" if state == "right" else "Buy"
    
    # Return the HTML template with the updated slider state and action
    return templates.TemplateResponse(
        "index.html", {"request": request, "state": state, "action": action}
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.2", port=8000)
