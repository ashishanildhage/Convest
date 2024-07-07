'''Libraries'''
# General Libraries
from datetime import datetime, timedelta

# Web Development Libraries
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# Broker Libraries
from pya3 import * #alice_blue


app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Initialize AliceBlue client (don't share these credentials)
alice = Aliceblue(user_id='347073', api_key='hLUQC1yiRaXIsCyfsW775JtcpFzT9obCHF7TVh1FBnoYosurv9CLIA4KWAZ0RRHMWIXMrtRTFNlPUTg6WitSq6cRICLNutiATkhINUmL5aqxTLkCf9rF09ALPgKFFZff')

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("display.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def index_post(request: Request, symbol: str = Form(...)):
    try:
        # Get the instrument
        instrument = alice.get_instrument_by_symbol('NSE', symbol.upper())
        
        # Get current market data
        scrip_info = alice.get_scrip_info(instrument)
        
        # Get historical data for two weeks
        to_date = datetime.now()
        from_date = to_date - timedelta(days=14)
        historical_data = alice.get_historical(instrument, from_date, to_date, "1", False)
        
        # Calculate two weeks change
        if len(historical_data) >= 2:
            two_weeks_change = ((historical_data[-1]['Close'] / historical_data[0]['Close']) - 1) * 100
        else:
            two_weeks_change = 0
        
        output = [
            f"{scrip_info['LTP']}",
            f"{round(((scrip_info['LTP'] / scrip_info['Close']) - 1) * 100, 2)}",
            f"{scrip_info['Open']}",
            f"{scrip_info['High']}",
            f"{scrip_info['Low']}",
            f"{scrip_info['Close']}",
            f"{round(two_weeks_change, 2)}"
        ]
        
        return templates.TemplateResponse("display.html", {"request": request, "output": output})
    except Exception as e:
        return templates.TemplateResponse("display.html", {"request": request, "error": str(e)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)