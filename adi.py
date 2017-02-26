import requests
from bs4 import BeautifulSoup
from slacker import Slacker
from selenium import webdriver


slack = Slacker('') # Enter in your Slack token in the single quotation marks
driver = webdriver.PhantomJS()

pid = raw_input('Enter in the pid: ')
pid = pid.upper()
desired_size = raw_input('Enter in the size: ')
size = int(desired_size) - 6.5
new_size = size * 20
raw_size = new_size + 580
size_val = int(raw_size)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36'
                '(KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36'}

def product_page(pid):
    global product
    url = 'adidas.com'
    global page
    page = 'http://www.' + url + '/us/' + pid + '.html?'
    print 'Getting Adidas URL...'
    slack.chat.post_message('#adidas', 'Getting Adidas URL...') # Enter in your channel name where it says #adidas
    driver.get(page)
    title = driver.find_element_by_tag_name('h1')
    product = title.text
    print product
    slack.chat.post_message('#adidas', str(product)) # Enter in your channel name where it says #adidas

def ATC(pid,size):
    print 'Size requested: ' + str(desired_size)
    url = 'http://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Cart-MiniAddProduct?layer=Add%20To%20Bag%20overlay&pid=' + str(pid) + '_' + str(size_val) + '&Quantity=1&masterPid=' + str(pid) + 'add-to-cart-button=='
    driver.get(url)
    success = driver.find_element_by_xpath('//*[@id="minicart_overlay"]/div[1]/span')
    success_message = 'Successfully added to bag'
    if success.text == success_message:
        print 'Successfully added ' + str(product.lower()) + ' in a size ' + str(desired_size) + ' to cart!'
        slack.chat.post_message('#adidas', 'Successfully added ' + str(product.lower()) + ' in a size ' + str(desired_size) + ' to cart!') # Enter in your channel name where it says #adidas
    # driver.get(page)
    # captcha = driver.find_element_by_xpath('/html/body/div[2]')
    # driver.get(captcha)

def sitekey():
	soup = BeautifulSoup(page.text, 'html.parser')
	sitekey = soup.find('div', attrs={'class': 'g-recaptcha'})['data-sitekey']
	print sitekey.text

def main():
    product_page(pid)
    sitekey()
    ATC(pid,11)

main()
