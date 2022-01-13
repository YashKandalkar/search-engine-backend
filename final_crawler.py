#if code crashes on your end, try -> 
#pip install lxml urllib bs4 requests pandas

from urllib.request import urljoin
from bs4 import BeautifulSoup
import requests
from urllib.request import urlparse
import pandas as pd
import json


# method for crawling a url at next level
def level_crawler(input_url):
    links = set()
    temp_urls = set()
    current_url_domain = urlparse(input_url).netloc
  
    beautiful_soup_object = BeautifulSoup(requests.get(input_url).text, "lxml")

    for anchor in beautiful_soup_object.findAll("a"):
        href = anchor.attrs.get("href")
        if(href != "" or href != None):
            href = urljoin(input_url, href)
            href_parsed = urlparse(href)
            href = href_parsed.scheme
            href += "://"
            href += href_parsed.netloc
            href += href_parsed.path
            final_parsed_href = urlparse(href)
            is_valid = bool(final_parsed_href.scheme) and bool(final_parsed_href.netloc)
            if is_valid:
                if current_url_domain in href and href not in links:
                    #print(href)
                    links.add(href)
                    temp_urls.add(href)

    return temp_urls


# depth parameter is used to control the crawler. Input URL is the starting point.
def crawler(depth, input_url):

    links_set = set()

    if (depth == 0):
        print("Depth is zero, nothing to crawl!")

    if(depth == 1):
        links_set.update(level_crawler(input_url))
  
    else:
        stack = []
        x = 0
        stack.append(input_url)
        for j in range(depth):
            for count in range(len(stack)):
                #url = queue.pop(0)
                url = stack.pop(0)
                urls = level_crawler(url)
                for i in urls:
                    stack.append(i)
        
        links_set.update(stack)

    #print(links_set)
    
    #gives csv file, change that if need be. 
    links_set = list(links_set)
    links_set.sort()
    df = pd.DataFrame(links_set)
    df.to_csv("gfg_three.csv")

    dictJson = {}
    objs_to_export = []
    for n in range(len(links_set)):
        dictJson = {}
        dictJson["url"] = links_set[n]
        dictJson["text"] = "no text"
        objs_to_export.append(dictJson)

    JSON_PATH = "final_gfg_output.json"
    with open(JSON_PATH, "a") as out_file:
        for obj in objs_to_export:
            json.dump(obj, out_file)
            out_file.write('\n')
    

    return links_set

running_crawler = (crawler(2, "https://www.geeksforgeeks.org/how-to-read-content-of-geeksforgeeks-in-an-organized-way/"))

