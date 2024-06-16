import requests
import csv
import os

FILE = "deals.csv"

def main():
#Check if there is a file named deals.csv 
    if os.path.exists(FILE):
        os.remove(FILE)

    headers = ["Title", "Metacritic Link", "Steam Rating", "Normal Price", "Sale Price", "Deal Rating"]
    with open(FILE, 'w', newline='') as csvfile:
        headerwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        headerwriter.writerow(headers)

# Making a GET request 
    r = requests.get('https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15') 
  
# check status code for response received 
# success code - 200 
# print(r) 
  
# print content of request 
# print(r.content) 

    deals = r.json()
    parsedeals(deals)


def gamedealscsv(game):
# Put the game deals into a csv file
    with open(FILE, 'a', newline='') as csvfile:
        dealwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        dealwriter.writerow(game)

    
def parsedeals(deals):
#Listing out the game information      
    for deal in deals: 
        
        game = []
        title = deal["title"]
        metacritic = deal["metacriticLink"]
        steamrating = deal["steamRatingText"]
        normal = deal["normalPrice"]
        sale = deal["salePrice"]
        rating = deal["dealRating"]    

#Adding to the list
        game.append(title)
        game.append(metacritic)
        game.append(steamrating)
        game.append(normal)
        game.append(sale)
        game.append(rating)
        gamedealscsv(game)







if __name__ == "__main__":
    main()
