from bs4 import BeautifulSoup
import requests
from datetime import datetime


def scrape(link):
    html_file = requests.get(link).text
    soup = BeautifulSoup(html_file, 'lxml')
    search_results=[]
    card_list=soup.find_all("li",class_="result-row")
    for card in card_list:
        post_link=card.a['href']
        if len(card.a['class'])>=3:
            if card.a['class'][2]=="empty":
                image_list=[]
        else:
            image_ids=card.a['data-ids'].split(",")
            image_url=["https://images.craigslist.org/","_300x300.jpg"]
            image_list=[]
            for id in image_ids:
                unique_id=id.split(":")[1]
                url=image_url[0]+unique_id+image_url[1]
                image_list.append(url)
        posted_on=card.div.time['datetime']
        title=card.div.h3.text.strip()
        if card.find('span',class_="result-hood"):
            other_info=card.find('span',class_="result-hood").text.strip()
        else:
            other_info=""
        overall_post=(image_list,post_link,title,other_info,posted_on)
        search_results.append(overall_post)
    return search_results