from __future__ import division
print("Program starting, please wait.")
import time
import alpaca_trade_api as tradeapi
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from datetime import datetime
import urllib.request, json 
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome("/Applications/chromedriver",options=chrome_options)
api = tradeapi.REST(
        'PK231GPF9DA5URXHU6PV',
        'f45G8ttOL6SHYB9DHOyHkXN0Wej1LgbvDLx05nAf',
        'https://paper-api.alpaca.markets'
    )


dow = datetime.today().weekday()
d1 = datetime.now()
current_time = d1.strftime("%H:%M:%S")


while True:
    if (dow == 0 or 1 or 2 or 3 or 4) and current_time == "06:30:00":
        print("Program initiated at "+current_time)
        print("Retreiving data.")
        driver.get("https://www.benzinga.com/premarket/")


        ticker1 = driver.find_element_by_xpath("/html/body/main/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/a")
        change1 = driver.find_element_by_xpath("/html/body/main/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[4]")
        company1 = driver.find_element_by_xpath("/html/body/main/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]")
        price1 = driver.find_element_by_xpath("/html/body/main/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[3]")

        ticker2 = driver.find_element_by_xpath("/html/body/main/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[2]/td[1]/a")
        change2 = driver.find_element_by_xpath("/html/body/main/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[2]/td[4]")
        company2 = driver.find_element_by_xpath("/html/body/main/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[2]/td[2]")
        price2 = driver.find_element_by_xpath("/html/body/main/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[2]/td[3]")

        ticker3 = driver.find_element_by_xpath("/html/body/main/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[3]/td[1]/a")
        change3 = driver.find_element_by_xpath("/html/body/main/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[3]/td[4]")
        company3 = driver.find_element_by_xpath("/html/body/main/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[3]/td[2]")
        price3 = driver.find_element_by_xpath("/html/body/main/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[3]/td[3]")

        print("Ticker"+" "+"Company"+" "+"PM Change"+"Price")
        print("------------------------")
        print(ticker1.text+" "+company1.text+" "+change1.text+" "+price1.text)
        print(ticker2.text+" "+company2.text+" "+change2.text+" "+price2.text)
        print(ticker3.text+" "+company3.text+" "+change3.text+" "+price3.text)

        purgedprice1p = (price1.text[1:])
        purgedprice2p = (price2.text[1:])
        purgedprice3p = (price3.text[1:])

        purgedprice1 = float(purgedprice1p)
        purgedprice2 = float(purgedprice2p)
        purgedprice3 = float(purgedprice3p)

        time.sleep(3600)

        with urllib.request.urlopen("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol="+ticker1.text+"&apikey=1ZTZ67D0EN7Y1F85") as url:
            data1 = json.loads(url.read().decode())
            gp1 = (data1["Global Quote"])
            curprice1a = (gp1["05. price"])
            curprice1 = float(curprice1a)

        with urllib.request.urlopen("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol="+ticker2.text+"&apikey=1ZTZ67D0EN7Y1F85") as url:
            data2 = json.loads(url.read().decode())
            gp2 = (data2["Global Quote"])
            curprice2a = (gp2["05. price"])
            curprice2 = float(curprice2a)

        with urllib.request.urlopen("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol="+ticker3.text+"&apikey=1ZTZ67D0EN7Y1F85") as url:
            data3 = json.loads(url.read().decode())
            gp3 = (data3["Global Quote"])
            curprice3a = (gp3["05. price"])
            curprice3 = float(curprice3a)




        percent_diff1 = ((curprice1 - purgedprice1)/purgedprice1) * 100
        percent_diff2 = ((curprice2 - purgedprice2)/purgedprice2) * 100
        percent_diff3 = ((curprice3 - purgedprice3)/purgedprice3) * 100



        if percent_diff1 < -10:
            api.submit_order(
            symbol=ticker1.text,
            qty=100,
            side='sell',
            type='market',
            time_in_force='gtc'
            )  
            print(ticker1.text + " bought")
        else:
            print(ticker1.text + " not bought")



        if percent_diff2 < -10:
            api.submit_order(
            symbol=ticker2.text,
            qty=100,
            side='sell',
            type='market',
            time_in_force='gtc'
            )
            print(ticker2.text + " bought")
        else:
            print(ticker2.text + " not bought")

        if percent_diff3 < -10:
            api.submit_order(
            symbol=ticker3.text,
            qty=100,
            side='sell',
            type='market',
            time_in_force='gtc'
            )
            print(ticker3.text + " bought")
        else:
            print(ticker3.text + " not bought")
    