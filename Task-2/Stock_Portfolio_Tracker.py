import streamlit as st
import requests

# Set API key here or load from secret
API_KEY = "BZ1H5LJ6M26FUYIL"

# Fetch stock data
def get_stock_data(symbol):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    try:
        quote = data["Global Quote"]
        return {
            "symbol": symbol,
            "price": float(quote["05. price"]),
            "change_percent": float(quote["10. change percent"].replace("%", ""))
        }
    except (KeyError, ValueError):
        return None

# Initialize session state
if "portfolio" not in st.session_state:
    st.session_state.portfolio = []

st.title("📊 Stock Portfolio Tracker")

# Input form
with st.form("add_stock_form"):
    col1, col2 = st.columns([2, 1])
    with col1:
        symbol = st.text_input("Stock Symbol (e.g., AAPL, TSLA)", max_chars=10)
    with col2:
        quantity = st.number_input("Quantity", min_value=1, value=1)
    submitted = st.form_submit_button("Add Stock")

    if submitted and symbol:
        symbol = symbol.upper()
        if not any(s['symbol'] == symbol for s in st.session_state.portfolio):
            data = get_stock_data(symbol)
            if data:
                st.session_state.portfolio.append({**data, "quantity": quantity})
                st.success(f"Added {symbol} to portfolio.")
            else:
                st.error("Invalid stock symbol or API limit reached.")
        else:
            st.warning("Stock already in portfolio.")

# Show portfolio
if st.session_state.portfolio:
    st.subheader("📈 Current Portfolio")
    total_value = 0

    for stock in st.session_state.portfolio:
        col1, col2, col3, col4, col5 = st.columns([1.5, 2, 2, 2, 1])
        col1.markdown(f"**{stock['symbol']}**")
        col2.markdown(f"Price: ${stock['price']:.2f}")
        col3.markdown(f"Change: {stock['change_percent']:.2f}%")
        value = stock["quantity"] * stock["price"]
        total_value += value
        col4.markdown(f"Value: ${value:,.2f}")
        if col5.button("🗑️ Remove", key=stock['symbol']):
            st.session_state.portfolio = [s for s in st.session_state.portfolio if s['symbol'] != stock['symbol']]
            st.rerun()

    st.markdown(f"### 💰 Total Portfolio Value: ${total_value:,.2f}")
else:
    st.info("Add some stocks to get started!")