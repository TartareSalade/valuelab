from abc import ABC, abstractmethod 


class MarketDataProvider:
    """
    Abstract class for market data providers
    With this class we can use different market data providers (yfinance in my case) without changing the code
    """
    @abstractmethod
    def get_company_profile(ticker: str) -> None:
        """
        Get the company profile for a given ticker. (General information about the company)
        :param ticker: The ticker of the company. (ticker is tag used to get company info)
        #TODO return CompanyProfile object
        """
        pass 
    @abstractmethod
    def get_market_snapshot(ticket: str) -> None:
        """
        Get the market snapshot for a give ticker.
        :param ticket: The ticker of the company. (ticker is tag used to get company info)²
        #TODO return MarketSnapshot object
        """
        pass

