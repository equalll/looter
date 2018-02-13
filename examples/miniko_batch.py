"""
A simple linear spider, you can crawl whole site slowly with it.
""" 
from crawltools import *
def download(url):
    src = get_source(url)
    links = src.cssselect('a.directlink')
    save_imgs(links)

if __name__ == '__main__':
    tasklist = reversed(list(f'https://konachan.net/post?page={9777-i}' for i in range(1, 9777)))
    r = [download(task) for task in tasklist]
