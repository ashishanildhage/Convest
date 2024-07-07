import React, { useState } from 'react';
import './TradingInterface.css';

const TradingInterface = () => {
  const [orderType, setOrderType] = useState('Buy');
  const [symbol, setSymbol] = useState('ITC');
  const [quantity, setQuantity] = useState(1);
  const [price, setPrice] = useState(245);
  const [productType, setProductType] = useState('Longterm');
  const [orderMode, setOrderMode] = useState('Regular');
  const [isMarket, setIsMarket] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Order submitted:', { orderType, symbol, quantity, price, productType, orderMode, isMarket });
    // Here you would typically send the order to your backend
  };

  return (
    <div className="trading-interface">
      <h2>{orderType} {symbol} NSE x {quantity} Qty</h2>
      <div className="price-info">
        <span>BSE: ₹241.45</span>
        <span>NSE: ₹241.50</span>
      </div>
      <form onSubmit={handleSubmit}>
        <div className="order-types">
          <button type="button" className={orderMode === 'Regular' ? 'active' : ''} onClick={() => setOrderMode('Regular')}>Regular</button>
          <button type="button" className={orderMode === 'Cover' ? 'active' : ''} onClick={() => setOrderMode('Cover')}>Cover</button>
          <button type="button" className={orderMode === 'AMO' ? 'active' : ''} onClick={() => setOrderMode('AMO')}>AMO</button>
        </div>
        <div className="product-types">
          <label>
            <input type="radio" name="productType" value="Intraday" checked={productType === 'Intraday'} onChange={() => setProductType('Intraday')} />
            Intraday
          </label>
          <label>
            <input type="radio" name="productType" value="Longterm" checked={productType === 'Longterm'} onChange={() => setProductType('Longterm')} />
            Longterm
          </label>
        </div>
        <div className="order-details">
          <label>
            Qty:
            <input type="number" value={quantity} onChange={(e) => setQuantity(e.target.value)} min="1" />
          </label>
          <label>
            Price:
            <input type="number" value={price} onChange={(e) => setPrice(e.target.value)} step="0.05" />
          </label>
        </div>
        <div className="order-type">
          <label>
            <input type="radio" name="orderType" value="Market" checked={isMarket} onChange={() => setIsMarket(true)} />
            Market
          </label>
          <label>
            <input type="radio" name="orderType" value="Limit" checked={!isMarket} onChange={() => setIsMarket(false)} />
            Limit
          </label>
        </div>
        <div className="margin-info">
          Margin required: ₹241.50
        </div>
        <div className="action-buttons">
          <button type="submit" className="buy-button">Buy</button>
          <button type="button" className="cancel-button">Cancel</button>
        </div>
      </form>
    </div>
  );
};

export default TradingInterface;


// import React, { useState, useEffect } from 'react';
// import axios from 'axios';
// import './TradingInterface.css';

// const API_URL = 'http://localhost:8000';

// const TradingInterface = () => {
//   const [orderType, setOrderType] = useState('Buy');
//   const [symbol, setSymbol] = useState('ITC');
//   const [quantity, setQuantity] = useState(1);
//   const [price, setPrice] = useState(245);
//   const [productType, setProductType] = useState('Longterm');
//   const [orderMode, setOrderMode] = useState('Regular');
//   const [isMarket, setIsMarket] = useState(false);
//   const [marketPrices, setMarketPrices] = useState({ BSE: 0, NSE: 0 });

//   useEffect(() => {
//     fetchMarketPrices();
//   }, [symbol]);

//   const fetchMarketPrices = async () => {
//     try {
//       const response = await axios.get(`${API_URL}/market_price/${symbol}`);
//       setMarketPrices(response.data);
//     } catch (error) {
//       console.error('Error fetching market prices:', error);
//     }
//   };

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     try {
//       const response = await axios.post(`${API_URL}/place_order`, {
//         symbol,
//         quantity: parseInt(quantity),
//         order_type: isMarket ? 'market' : 'limit',
//         price: isMarket ? undefined : parseFloat(price),
//         product_type: productType,
//         order_mode: orderMode
//       });
//       console.log('Order placed:', response.data);
//       alert('Order placed successfully!');
//     } catch (error) {
//       console.error('Error placing order:', error);
//       alert('Failed to place order. Please try again.');
//     }
//   };

//   // ... (rest of the component remains the same)

//   return (
//     <div className="trading-interface">
//       <h2>{orderType} {symbol} NSE x {quantity} Qty</h2>
//       <div className="price-info">
//         <span>BSE: ₹{marketPrices.BSE}</span>
//         <span>NSE: ₹{marketPrices.NSE}</span>
//       </div>
//       {/* ... (rest of the JSX remains the same) */}
//     </div>
//   );
// };

// export default TradingInterface;