class CompanyProfile:
    """
    Class representing a company profile.
    """
    def __init__(self, ticker: str, name: str, sector: str, country: str, market_index: str, currency: str):
        self.ticker = ticker
        self.name = name
        self.sector = sector
        self.country = country
        self.market_index = market_index
        self.currency = currency
    
    