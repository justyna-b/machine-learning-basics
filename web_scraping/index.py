import requests
from bs4 import BeautifulSoup
import string
import random
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('web-scrap-py-d071b481aaa1.json', scope)

# authorize the clientsheet
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open('Brzezinska-175')
sheet.add_worksheet(rows=5,cols=4, title='Giełda')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(1)

def random_char(y):
    return ''.join(random.choice(string.ascii_lowercase) for x in range(y))

rnd_shortcut = ''
tries = 0
max_tries = 5
while tries < max_tries:
    rnd_shortcut = (random_char(3))
    url = f'https://stooq.pl/q/?s={rnd_shortcut}'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    results = soup.find('span', id=f'aq_{rnd_shortcut}_c2')
    if results != None:
        zmiana = soup.find('span', id=f'aq_{rnd_shortcut}_m2')
        transakcja = soup.find('span', id=f'aq_{rnd_shortcut}_n1')
        print(zmiana.text, results.text, transakcja.text)
        sheet_instance.update(f'A{tries + 1}', rnd_shortcut)
        sheet_instance.update(f'B{tries + 1}', zmiana.text)
        sheet_instance.update(f'C{tries + 1}', results.text)
        sheet_instance.update(f'D{tries + 1}', transakcja.text)
        tries += 1
        rnd_shortcut = ''

#2-----------------------------------------------------------------

sheet.add_worksheet(rows=15, cols=1, title='Linki')
link_instance = sheet.get_worksheet(2)
url= 'https://www.diki.pl/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
i = 1
for link in soup.find_all('a'):
    reLink = link.get('href')
    try:
        reLink = link.get('href')
        if(reLink[0] != '/' and len(reLink) > 3):
            link_instance.update(f'A{i}', reLink)
            i += 1
    except TypeError:
        pass

#3------------------------------------------------------------------

sheet.add_worksheet(rows=1, cols=4, title='Filmweb')
filmweb_instance = sheet.get_worksheet(3)
url= 'https://www.filmweb.pl/film/Pulp+Fiction-1994-1039'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
director = soup.find('span', itemprop ='name')
filmweb_instance.update('A1', director.text)
boxoffice_section = soup.find('div', class_='filmOtherInfoSection__group')
boxoffice = boxoffice_section.find('div', class_='filmInfo__info')
filmweb_instance.update('B1', boxoffice.text)
rating = soup.find('span', class_='filmRating__rateValue')
filmweb_instance.update("C1", rating.text)
base = 'https://www.filmweb.pl'
idxStart = len(base)
splitUrl = f'{url[idxStart:]}/dates'
release = soup.find('a', href=splitUrl)
filmweb_instance.update('D1', release.text)






