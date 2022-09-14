import csv
from tkinter import E
from bs4 import BeautifulSoup
import requests

""" with open('sample.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml') """

# print(soup.prettify())

# match = soup.title.text
# match = soup.div

""" # fist 'div'
match = soup.find('div') """

""" footer = soup.find('div', class_='footer')
print(footer) """

""" article = soup.find('div', class_='article')
# print(article)

headline = article.h2.a.text
summary = article.p.text
print(headline)
print(summary) """

""" for article in soup.findAll('div', class_='article'):
    headline = article.h2.a.text
    summary = article.p.text

    print(headline)
    print(summary) """

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

csv_file = open('cms_scrape.csv','w')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['headline','summary','video_link'])

articles = soup.find_all('article')


for article in articles:

    headline = article.h2.a.text 
    print(headline)

    summary = article.find('div', class_='entry-content').p.text    
    print(summary)

    try:

        video_src = article.find('iframe', class_='youtube-player')['src']

        video_id = video_src.split('/')[4].split('?')[0]

        youtube_link = f'https://youtube.com/watch?v={video_id}'
    except Exception as e:
        youtube_link = None

    print(youtube_link)
    print()

    csv_writer.writerow([headline,summary,youtube_link])

csv_file.close()
