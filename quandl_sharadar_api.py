import requests


class Equity(object):

    def __init__(self, ticker, api_key=None):
        self.api_key = api_key or  QUANDL_API_KEY
        self.host = 'https://www.quandl.com/api/v3/datatables/SHARADAR/SF1.json'
        self.params = {'api_key': self.api_key, 'ticker': ticker, 'dimension': 'MRY', 'qopts.latest': 1, 'qopts.columns': 'eps,pe1,currentratio,divyield,dps,de,roa,roe,roic'}

    @property
    def company_data(self):
        resp = requests.get(self.host, params=self.params)
        data = resp.json()['datatable']
        data_dict = {}
        count = 0
        if data['data']:
            for col in data['columns']:
                data_dict.update({col['name'] : data['data'][0][count]})
                count +=1
        return data_dict

    @property
    def eps(self):
        data = self.company_data
        eps = data.get('eps', None)
        return eps

    @property
    def pe(self):
        data = self.company_data
        pe = data.get('pe1', None)
        return pe 
    
    @property
    def current_ratio(self):
        data = self.company_data
        current_ratio = data.get('currentratio', None)
        return current_ratio
    
    @property
    def dividend_yield(self):
        data = self.company_data
        div_yield = data.get('divyield', None)
        return div_yield
    
    @property
    def dividend_per_share(self):
        data = self.company_data
        dividend_per_share = data.get('dps', None)
        return dividend_per_share
    
    @property
    def debt_equity_ratio(self):
        data = self.company_data
        debt_equity_ratio = data.get('de', None)
        return debt_equity_ratio

    @property
    def return_on_assets(self):
        data = self.company_data
        return_on_assets = data.get('roa', None)
        return return_on_assets
    
    @property
    def return_on_equity(self):
        data = self.company_data
        return_on_equity = data.get('roe', None)
        return return_on_equity
    
    @property
    def return_on_invest_capital(self):
        data = self.company_data
        return_on_invest_capital = data.get('roic', None)
        return return_on_invest_capital
