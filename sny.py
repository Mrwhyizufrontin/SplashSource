import requests
import sys
import itertools
from time import sleep
from bs4 import BeautifulSoup
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.support.ui import Select


vision = raw_input('Do you fw the vision? Y/N: ')
if vision == 'Y' or vision == 'y':
    print colored('Let`s build', 'red')
elif vision != 'Y' or vision != 'y':
    print colored('You are washed! Goodbye', 'red')
    sys.exit(colored('Exiting now', 'red'))

supreme_text = '''
$$$$$$$$$$$$$$$$$       $$$           $$$       $$$$$$$$$$$$$$$$$       $$$$$$$$$$$$$$$$$       $$$$$$$$$$$$$$$$$       $$$$$$   $$$$$$     $$$$$$$$$$$$$$$$$
$$$                     $$$           $$$       $$$           $$$       $$$           $$$       $$$                     $$$ $$$ $$$ $$$     $$$
$$$$$$$$$$$$$$$$$       $$$           $$$       $$$$$$$$$$$$$$$$$       $$$$$$$$$$$$$$$$$       $$$$$$$$$$$$$$$$$       $$$  $$$$   $$$     $$$$$$$$$$$$$$$$$
              $$$       $$$           $$$       $$$                     $$$        $$$          $$$                     $$$         $$$     $$$
$$$$$$$$$$$$$$$$$       $$$$$$$$$$$$$$$$$       $$$                     $$$           $$$       $$$$$$$$$$$$$$$$$       $$$         $$$     $$$$$$$$$$$$$$$$$'''
print colored(supreme_text, 'red')

print '\nChoose a number from the options below'

options = raw_input('\t\tOptions:\n\t\t1 for jackets\n\t\t2 for shirts\n\t\t3 for tops/sweaters\n\t\t4 for sweatshirts\n\t\t5 for pants\n\t\t6 for hats\n\t\t7 for accessories\n\t\t8 for shoes\n\t\t9 for skate\nEnter: ')

base_url = 'http://www.supremenewyork.com/shop/'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36'
                '(KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36'}

def supreme(options):
    global products
    global page
    global product_page

    requests.get(base_url)

    if options == '1':
        page = 'all/jackets'
    elif options == '2':
        page = 'all/shirts'
    elif options == '3':
        page = 'all/tops_sweaters'
    elif options == '4':
        page = 'all/sweatshirts'
    elif options == '5':
        page = 'all/pants'
    elif options == '6':
        page = 'all/hats'
    elif options == '7':
        page = 'all/accessories'
    elif options == '8':
        page = 'all/shoes'
    elif options == '9':
        page = 'all/skate'

    product_page = base_url + str(page)
    page = requests.get(product_page, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    items = []
    color = []

    for products in soup.findAll('h1')[1:]:
        products = products.text
        items.append(products)

    for colors in soup.findAll('p'):
        colors = colors.text
        color.append(colors)

    combined =  list(itertools.chain(*zip(items, color)))
    combined = str(combined).replace('[', '')
    combined = str(combined).replace("u'", "")
    combined = str(combined).replace("'", "")
    combined = str(combined).replace(']', '')

    print 'Products and colors are below: \n' + colored(combined.encode('utf-8'), 'cyan')
    return items, color

def checkout(item, clr):

    correct_product = False # Leave this as it is
    correct_color = False # Leave this as it is

    while not correct_product:
        choose_products = raw_input(colored('Enter in a product from the products above: ', 'yellow'))
        if choose_products not in item:
            print colored('Invalid product!!!', 'red')
        else:
            correct_product = True # Leave this as it is

    while not correct_color:
        choose_colors = raw_input(colored('Enter in a color from the colors above: ', 'yellow'))
        if choose_colors not in clr:
            print colored('Invalid color!!!', 'red')
        else:
            correct_color = True # Leave this as it is

    checkoutUrl = 'https://www.supremenewyork.com/checkout' # Leave this as it is
    sizeOption = 'Medium' # Enter in a size you want, either pants size or shirt/pant size. Comment this line out if the item does not have a size
    name = 'John Doe' # Enter in your name
    email = 'Test@example.com' # Enter in your email
    phoneNum = '5555555555' # Enter in your phone number
    address1 = '1600 Pennsylvania Avenue NW' # Enter in your address
    address2 = 'Apartment 123' # Enter in your apartment/unit/etc number if applicable
    city = 'Compton' # Enter in your city
    zipcode = '20500' # Enter in your zipcode
    state = 'DC' # Enter in your state abbreviation
    country = 'USA' # Enter in your country abbreviation
    ccType = 'Visa'  # Enter in your card type Visa, Mastercard, or American Express
    ccNum = '5274576954806318'  # Enter in your card number
    ccMonth = '06'  # Enter in your card's expiration month
    ccYear = '2019'  # Enter in your card's expiration year in the formay YYYY

    driver = webdriver.Chrome() # You can change this to phantomJS if you don't want a window to pop up
    driver.get(product_page)

    product_select = driver.find_element_by_xpath('//*[@id="container"]/article[' + str(item.index(choose_products) + 1) + ']/div/h1/a[contains(text(), choose_products)]')
    product_select.click()
    sleep(0.5)

    size = Select(driver.find_element_by_xpath('//*[@id="size"]'))
    size.select_by_visible_text(sizeOption)
    sleep(0.5)

    atc_button = driver.find_element_by_name('commit')
    atc_button.click()
    sleep(0.5)

    checkout_button = driver.find_element_by_xpath('//*[@id="cart"]/a[2]')
    checkout_button.click()
    sleep(0.5)

    driver.get(checkoutUrl)

    flname = driver.find_element_by_id('order_billing_name')
    flname.send_keys(name)

    Email = driver.find_element_by_id('order_email')
    Email.send_keys(email)

    phone_num = driver.find_element_by_id('order_tel')
    phone_num.send_keys(phoneNum)

    Address1 = driver.find_element_by_id('bo')
    Address1.send_keys(address1)

    Address2 = driver.find_element_by_id('oba3')
    Address2.send_keys(address2)

    Zipcode = driver.find_element_by_id('order_billing_zip')
    Zipcode.send_keys(zipcode)

    City = driver.find_element_by_id('order_billing_city')
    City.send_keys(city)

    State = Select(driver.find_element_by_id('order_billing_state'))
    State.select_by_visible_text(state)

    Country = Select(driver.find_element_by_id('order_billing_country'))
    Country.select_by_visible_text(country)

    save_address = driver.find_element_by_id('store_address') # Line of potential error 168 and 169
    save_address.click()

    card_type = Select(driver.find_element_by_id('credit_card_type'))
    card_type.select_by_visible_text(ccType)

    card_number = driver.find_element_by_xpath('//*[@id="cnb"]')
    card_number.send_keys(ccNum)

    card_month = driver.find_element_by_id('credit_card_month')
    card_month.send_keys(ccMonth)

    card_year = driver.find_element_by_id('credit_card_year')
    card_year.send_keys(ccYear)

    terms_button = driver.find_element_by_xpath('//*[@id="order_terms"]') # Line of potential error 183 and 184
    terms_button.click()

    finalize_order = driver.find_element_by_xpath('//*[@id="pay"]/input')
    finalize_order.click()

item, clr = supreme(options)
checkout(item, clr)
