import requests
import pytest
import re

from datetime import datetime

class TestBeerVals:
    after_month = 12
    after_year = 2015

    after_date = datetime(after_year, after_month, 1)

    @pytest.fixture
    def beer_data(self):
        response = requests.get(f"https://api.punkapi.com/v2/beers?brewed_after={self.after_month}-{self.after_year}")
        assert response.status_code == 200
        return response.json()

    def test_abv(self, beer_data):
        for beer in beer_data:
            abv = beer["abv"]
            assert abv is not None
            assert abv != ""
            assert type(abv) is float
            assert abv > 4.0

    def test_beer_name(self, beer_data):
        for beer in beer_data:
            name = beer["name"]
            assert name is not None
            assert name != ""

    def test_ebc_srm(self, beer_data):
        for beer in beer_data:
            ebc = beer["ebc"]
            srm = beer["srm"]
            assert ebc is not None
            assert ebc > 0
            assert srm is not None
            assert srm > 0
            assert srm * 1.97 <= ebc <= srm * 2

    def test_date(self, beer_data):
        for beer in beer_data:
            date = beer["first_brewed"]
            assert date is not None
            assert date != ""
            assert re.match(r"\d{2}\/\d{4}", date)
            month, year = (int(i) for i in date.split('/'))
            first_brew_date = datetime(year, month, 1)
            assert first_brew_date > self.after_date