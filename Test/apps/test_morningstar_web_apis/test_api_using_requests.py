import requests

url = 'http://financials.morningstar.com/ajax/ReportProcess4CSV.html?t=TWTR&reportType=is&period=12&dataType=A&order=asc&columnYear=10&number=3'
resp = requests.get(url)
print(resp.text)