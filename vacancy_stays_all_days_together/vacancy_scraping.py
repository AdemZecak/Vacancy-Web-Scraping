from bs4 import BeautifulSoup
import requests
from csv import writer
import calendar
from datetime import date, datetime
import csv



c = calendar.Calendar()
x = datetime.now()
 
year = x.year
month = x.month


date_list = []

for date in c.itermonthdates(year, month):
    date_list.append(str(date))


urls = [str(url) for url in range(2,8)]

with open("vacancy_scraping.csv","w",encoding="utf8",newline="") as f:

            thewriter = writer(f)
            header = ["Price for 2 days"]
            thewriter.writerow(header)


            for num in urls: 

                print("This is new round for",num,"nights")

                for date in date_list:
                    
                    url = "https://www.centerparcs.fr/fr-fr/co_vacances-france?market=fr&language=fr&c=CPE_GEO&univers=cpe&type=COUNTRY&item=FR&currency=EUR&group=offer&sort=popularity&asc=asc&page=1&nb=30&displayPrice=default&dateuser=1&facet[DATE]="+ date +"&facet[DURATIONCP][]="+ num +"&facet[COUNTRYSITE][]=l1_FR&facet[PARTICIPANTSCP][adult]=2&facet[PARTICIPANTSCP][senior]=0&facet[PARTICIPANTSCP][pet]=0"
                    page = requests.get(url)

                    soup = BeautifulSoup(page.content,"html.parser")
                    price = soup.find_all(name="span",class_="cartoucheDomain-priceValue")
                    print("")
                    print(date)
                    print("")


                    for i in price:

                        price = soup.find(name="span",class_="cartoucheDomain-priceValue").text
                        thewriter.writerow(i)
                        print(i.text)
                        days = "New round of stays"

                thewriter.writerow(days)




                
                            
