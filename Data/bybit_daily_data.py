from bs4 import BeautifulSoup
import requests
import time

def extract_tickers(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        ticker_tags = soup.find_all('a')
        
        tickers = [ticker.text for ticker in ticker_tags]
        return tickers
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None
    
def ticker_cleaner(input_strings, substrings_to_remove):
    cleaned_tickers = []
    for ticker in input_strings:
        cleaned_ticker = ticker
        for substring in substrings_to_remove:
            cleaned_ticker = cleaned_ticker.replace(substring, '')
        cleaned_tickers.append(cleaned_ticker)
    return cleaned_tickers


url = 'https://public.bybit.com/trading/'
tickers = extract_tickers(url)
data_remove = tickers
remove_data = '/'

clean_data = ticker_cleaner(data_remove, remove_data)

date_select = input('Enter dates in format YEAR-MONTH-DAYS: ')

for cleaned_ticker in clean_data:
    time.sleep(2)
    file_url = f'https://public.bybit.com/trading/{cleaned_ticker}/{cleaned_ticker}{date_select}.csv.gz'
    response = requests.get(file_url)
    
    if response.status_code == 200:
        with open(f'{cleaned_ticker}{date_select}.csv.gz', 'wb') as file:
            file.write(response.content)
        print(f"File downloaded: {cleaned_ticker}{date_select}.csv.gz")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
