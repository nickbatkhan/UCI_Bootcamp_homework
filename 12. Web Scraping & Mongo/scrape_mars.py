import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_data = {}

    # # News
    url_mars = 'https://mars.nasa.gov/news'
    browser.visit(url_mars)
    time.sleep(5)

    html_mars = browser.html
    soup_mars = bs(html_mars, 'html.parser')

    news_title = soup_mars.find("div", class_="content_title").text
    news_p = soup_mars.find('div', class_="article_teaser_body").text
    mars_data["news_title"] = (news_title)
    mars_data["news_p"] = (news_p)


    # # JPL
    url_jpl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_jpl)
    time.sleep(5)

    html_jpl = browser.html
    soup_jpl = bs(html_jpl, 'html.parser')

    featured_image_url = soup_jpl.find_all("footer")
    test=featured_image_url[0]
    s = str(test)
    start = 'data-link="/spaceimages/details.php?id='
    end = '" data-title'
    startindex = s.find(start)+len(start)
    endindex = s.find(end)
    file = s[startindex:endindex]
    
    url_jpl_hires = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/'+file+'_hires.jpg'
    mars_data["featured_image_url"] = url_jpl_hires


    # # Mars Weather
    url_twitter = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url_twitter)
    time.sleep(5)

    html_twitter = browser.html
    soup_twitter = bs(html_twitter, 'html.parser')

    mars_weather = soup_twitter.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    mars_data["mars_weather"] = mars_weather


    # # Mars Facts
    mars_facts = 'https://space-facts.com/mars/'
    d = pd.read_html(mars_facts)
    
    facts = pd.DataFrame(d[0])
    facts.columns = ['Fields', 'Values']

    facts_html = facts.to_html()
    mars_data["mars_facts"] = facts_html


    # # Mars Hemis
    url_hemis = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_hemis)
    time.sleep(5)

    html_hemis = browser.html
    soup_hemis = bs(html_hemis, 'html.parser')

    hemisphere_image_urls = []
    hemis = {}

    for i in range(4):
        action = browser.find_by_tag('h3')
        action[i].click()
        time.sleep(3)
        html = browser.html
        soup = bs(html, 'html.parser')
        img_url = soup.find('img', class_='wide-image')['src']
        hemis_title = soup.find('h2',class_='title').text
        hemis_url = 'https://astrogeology.usgs.gov/'+ img_url
        hemis = {'title': hemis_title, 'img_url': hemis_url}
        hemisphere_image_urls.append(hemis)
        browser.back()

    #print(hemisphere_image_urls)

    mars_data["hemisphere_images"] = hemisphere_image_urls

    # Close the browser after scraping
    browser.quit()
    
    return mars_data