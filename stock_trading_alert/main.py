import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# !!!: Timezone difference
alpha_api_key = "0QUV2DT6F7SIFNFN"
news_api_key = "00263b7b34be410c83fdbebe753da46a"

paramaters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_api_key,
    "outputsize": "compact"
}

response = requests.get(url="https://www.alphavantage.co/query", params=paramaters)
response.raise_for_status()
daily_data = response.json()

last_2_days = list(daily_data["Time Series (Daily)"])[:2]
data_last_2_days = {key : daily_data["Time Series (Daily)"][key] for key in last_2_days}

ytd_close_price = float(data_last_2_days[last_2_days[0]]["4. close"])
day_before_close_price = float(data_last_2_days[last_2_days[1]]["4. close"])
delta_close = ytd_close_price - day_before_close_price
volume_of_change = round(abs(delta_close/ytd_close_price), 2)

if volume_of_change < 0.05:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    # Flaw: time of publish is not necessarily aligned with stock price time
    # definition of the first 3 news pieces?
    news_parameters = {
    "apiKey": news_api_key,
    "q": "Tesla",
    # "country": "us"
    # "category": "business, technology"
}
    response = requests.get(url="https://newsapi.org/v2/top-headlines", params=news_parameters)
    response.raise_for_status()
    news_data = response.json()
    no_of_articles = len(["articles"])

    try:
        news_headlines = [news_data["articles"][i]["title"] for i in range(3)]
    except IndexError:
        if  no_of_articles > 0:
            news_headlines = [news_data["articles"][i]["title"] for i in range(no_of_articles)]
        else:
            news_headlines = "No articles available for the stock."
    finally:
        print(news_headlines)
    
    if delta_close < 0:
        symbol = "↑"
    else:
        symbol = "↓"

    message_body = ""
    for index, headline in enumerate(news_headlines):
        message_body += f"Headline {index+1}: {headline}\n"    

    message_body = f"{STOCK}: {symbol} {volume_of_change*100}%\n{message_body}"
    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number. 
    account_sid = 'AC4322edaf40ba4e3f6157c61230129ed6'
    auth_token = '17f388aa26c17a489c99423c809c1f6a'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='+12563882868',
    to='+12046989527', 
    body= message_body
    )

else:
    print("Price change < 5%.")





 

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

