import requests
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.PhantomJS()
print 'Choose a number from the options below'
options = raw_input('\t\tOptions:\n\t\t1 for jackets\n\t\t2 for shirts\n\t\t3 for tops/sweaters\n\t\t4 for sweatshirts\n\t\t5 for pants\n\t\t6 for t-shirts\n\t\t7 for hats\n\t\t8 for bags\n\t\t9 for accessories\n\t\t10 for skate\n\t\t11 for all\nEnter: ')
base_url = 'http://www.supremenewyork.com/shop/'
def supreme(options):
    global page
    global product_page

    driver.get(base_url)

    if options == '1':
        page = 'all/jackets'
    if options == '2':
        page = 'all/shirts'
    if options == '3':
        page = 'all/tops_sweaters'
    if options == '4':
        page = 'all/sweatshirts'
    if options == '5':
        page = 'all/pants'
    if options == '6':
        page = 'all/t-shirts'
    if options == '7':
        page = 'all/hats'
    if options == '8':
        page = 'all/bags'
    if options == '8':
        page = 'all/accessories'
    if options == '10':
        page = 'all/skate'
    if options == '11':
        page = 'all'

    product_page = base_url + str(page)
    driver.get(product_page)

def products():
    soup = BeautifulSoup(product_page.content, 'html.parser')
    for item in soup.findAll("name-link"):
        print 'Item and color: ' + item.text

supreme(options)
products()
