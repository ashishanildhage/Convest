from alice_blue import * 
from pprint import pprint # Prints API output structure organised

def giveMoreDebugInfo(): # Provides more debug information when you enable logging
    import logging
    logging.basicConfig(level=logging.DEBUG) 
giveMoreDebugInfo() 

# ---------------------------------------

'''https://developers.aliceblueonline.com/apps
Redirect URL and Post Back URL - https://ant.aliceblueonline.com/plugin/callback.
Enter the App Code/ID and App Secret'''
username='347073'
access_token = AliceBlue.login_and_get_sessionID(username   = username, #6 digit No.
                                                password    = "AshishDhage@75225",
                                                twoFA       = "2000", #Year of Birth
                                                app_id      = "t3iAvQV2rLdma72", 
                                                api_secret  = "prOUeXEUmlfvZIHjIfWBjSzUGjZoqoHyFbXhoyiBmbOYdaYqyvzeDKvJedUQTurjgslUqNctMsbSffeBeInbuqRzSUWbiodglFtJ") 
print()

#Create an "alice" Object using session ID
alice = AliceBlue(username = username, session_id = access_token, master_contracts_to_download=['NSE', 'BSE']) 
print()

alice.get_instrument_by_symbol("NSE", "SBIN")

print(alice.get_instrument_by_symbol("NSE", "SBIN"))    

def place_order(order):
    order = Order(
        symbol = "SBIN",
        quantity = 2,
        order_type = "MARKET",
        product_type = "INTRADAY"
    )

    return order

print(place_order(alice))











# pip install fastapi uvicorn alice_blue










from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from alice_blue import AliceBlue  # Import your AliceBlue class

app = FastAPI()

# Initialize AliceBlue client
# Replace with your actual credentials
alice = AliceBlue(username='347073', password='1#Ashish1o1', api_secret='984651621465')

class Order(BaseModel):
    symbol: str
    quantity: int
    order_type: str
    price: Optional[float] = None

@app.post("/place_order")
async def place_order(order: Order):
    try:
        # Use your AliceBlue integration to place the order
        if order.order_type == "market":
            result = alice.place_order(
                symbol=order.symbol,
                quantity=order.quantity,
                order_type=alice.ORDER_TYPE_MARKET
            )
        elif order.order_type == "limit":
            if order.price is None:
                raise HTTPException(status_code=400, detail="Price is required for limit orders")
            result = alice.place_order(
                symbol=order.symbol,
                quantity=order.quantity,
                order_type=alice.ORDER_TYPE_LIMIT,
                price=order.price
            )
        else:
            raise HTTPException(status_code=400, detail="Invalid order type")
        
        return {"message": "Order placed successfully", "order_id": result.order_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/account_info")
async def get_account_info():
    try:
        # Use your AliceBlue integration to fetch account info
        balance = alice.get_balance()
        positions = alice.get_positions()
        return {"balance": balance, "positions": positions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from typing import Optional

# app = FastAPI()

# # Enable CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all methods
#     allow_headers=["*"],  # Allows all headers
# )

# class Order(BaseModel):
#     symbol: str
#     quantity: int
#     order_type: str
#     price: Optional[float] = None
#     product_type: str
#     order_mode: str

# @app.post("/place_order")
# async def place_order(order: Order):
#     try:
#         # This is where you would integrate with your actual trading system
#         # For now, we'll just return a mock response
#         return {
#             "message": "Order placed successfully",
#             "order_details": order.dict()
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.get("/market_price/{symbol}")
# async def get_market_price(symbol: str):
#     # This would typically fetch real market data
#     # For demonstration, we'll return mock data
#     mock_prices = {
#         "ITC": {"BSE": 241.45, "NSE": 241.50}
#     }
#     if symbol not in mock_prices:
#         raise HTTPException(status_code=404, detail="Symbol not found")
#     return mock_prices[symbol]

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)