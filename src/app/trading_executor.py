# trading_executor.py

class TradingExecutor:
    """
    A class to simulate submitting trades to a trading platform.
    In a real application, this would handle API calls to the exchange.
    """
    def __init__(self, symbol):
        """
        Initializes the TradingExecutor with the trading symbol.
        """
        self.symbol = symbol

    def buy(self):
        """
        Simulates submitting a buy order.
        """
        print(f"ACTION: BUY {self.symbol}")

    def sell(self):
        """
        Simulates submitting a sell order.
        """
        print(f"ACTION: SELL {self.symbol}")

    def hold(self):
        """
        Simulates deciding to hold the current position.
        """
        print(f"ACTION: HOLD {self.symbol}")