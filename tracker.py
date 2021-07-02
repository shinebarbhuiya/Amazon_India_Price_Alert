# This is a simple script to track the price of an Amazon  product.
# It notifies you when there is a drop in price.
# Written By Shine A. Barbhuiya


import requests
from bs4 import BeautifulSoup as BS
from smtplib import SMTP

# Asks the user to provide the URL link.
# URL = input("Enter the link of the amazon product: ")
URL = input("Enter The Link Of Amazon Product You Want To Track: ")

page = requests.get(URL, headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"})
soup= BS(page.content, "html.parser")

def name_scrape():
    """Scrape the name from the product page."""

    product_name = soup.find(id = "productTitle").text.strip()
    return product_name

def price_scrape():
    """Scrape the price and convert it into float"""
   
    price = float(soup.find(id = "priceblock_ourprice").text.split()[1].replace(",", ""))
    return price

# Here enter your email id and password. Also, you can add receiver id as well.  
SMTP_SERVER = "smtp.gmail.com"
PORT = 587
EMAIL_ID = ""
PASS = ""
RECEIVER_EMAIL = ""

def alert():
    """Alert you on your gmail by sending a mail."""

    server = SMTP(SMTP_SERVER, PORT)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_ID, PASS)

    subject = "Hurry! Buy Now!!!"
    body = f"Price of {name_scrape()} dropped. Hurry up and buy it asap. The link is - " + URL
    message = f"Subject : {subject}\n\nBody : {body}"

    # Send email from 1st email to the 2nd email. 
    # In this case I am sending from my email to me.
    server.sendmail(EMAIL_ID, EMAIL_ID, message)
    server.quit()


affordable_price = int(input("Enter an affordable price for this product: "))


if price_scrape() <= affordable_price:
    alert()



