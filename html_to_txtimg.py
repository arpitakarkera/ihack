"""
returns text and list of image urls from html
"""
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(soup):
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)

def image_from_html(soup):
    return [x['src'] for x in soup.findAll('img')]

def extract(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = text_from_html(soup)
    image_links = image_from_html(soup)
    return text, image_links
