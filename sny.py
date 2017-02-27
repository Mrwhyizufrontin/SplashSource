import requests
import urllib2
from bs4 import BeautifulSoup
from slacker import Slacker

slack = Slacker('')

print '''
$$$$$$$$$$$$$$$$$       $$$           $$$       $$$$$$$$$$$$$$$$$       $$$$$$$$$$$$$$$$$       $$$$$$$$$$$$$$$$$       $$$$$$   $$$$$$     $$$$$$$$$$$$$$$$$
$$$                     $$$           $$$       $$$           $$$       $$$           $$$       $$$                     $$$ $$$ $$$ $$$     $$$
$$$$$$$$$$$$$$$$$       $$$           $$$       $$$$$$$$$$$$$$$$$       $$$$$$$$$$$$$$$$$       $$$$$$$$$$$$$$$$$       $$$  $$$$   $$$     $$$$$$$$$$$$$$$$$
              $$$       $$$           $$$       $$$                     $$$        $$$          $$$                     $$$         $$$     $$$
$$$$$$$$$$$$$$$$$       $$$$$$$$$$$$$$$$$       $$$                     $$$           $$$       $$$$$$$$$$$$$$$$$       $$$         $$$     $$$$$$$$$$$$$$$$$'''

print '\nChoose a number from the options below'
options = raw_input('\t\tOptions:\n\t\t1 for jackets\n\t\t2 for shirts\n\t\t3 for tops/sweaters\n\t\t4 for sweatshirts\n\t\t5 for pants\n\t\t6 for t-shirts\n\t\t7 for hats\n\t\t8 for bags\n\t\t9 for accessories\n\t\t10 for skate\n\t\t11 for all\nEnter: ')
base_url = 'http://www.supremenewyork.com/shop/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36'
                '(KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36'}
global product_id
global variant
def supreme(options):
    global page
    global product_page

    requests.get(base_url)

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
    if options == '9':
        page = 'all/accessories'
    if options == '10':
        page = 'all/skate'
    if options == '11':
        page = 'all'

    product_page = base_url + str(page)
    page = requests.get(product_page, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    variants = []
    for products in soup.findAll('h1', 'p'):
        for colors in soup.findAll('p'):
            print 'Products: ' + products.text + '\nColor: ' + colors.text
        # slack.chat.post_message('#supreme', products.text)
    # print page.text



# def checkout():
#     checkout_page = 'https://www.supremenewyork.com/checkout.json'
#     checkoutHeaders={
#         'host':              'www.supremenewyork.com',
#         'If-None-Match':    '"*"',
#         'Accept':            'application/json',
#         'Proxy-Connection':  'keep-alive',
#         'Accept-Encoding':   'gzip, deflate',
#         'Accept-Language':   'en-us',
#         'Content-Type':      'application/x-www-form-urlencoded',
#         'Origin':            'http://www.supremenewyork.com',
#         'Connection':        'keep-alive',
#         'User-Agent':        'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257',
#         'Referer':           'http://www.supremenewyork.com/mobile'
#     }
#     payload = {
#         'store_credit_id':    '',
#         'from_mobile':              '1',
#         'cookie-sub':               '%7B%22'+str(variant)+'%22%3A1%7D',       # cookie-sub: eg. {"VARIANT":1} urlencoded
#         'same_as_billing_address':  '1',
#         'order[billing_name]':      'anon mous',                              # FirstName LastName
#         'order[email]':             'anon@mailinator.com',                    # email@domain.com
#         'order[tel]':               '999-999-9999',                           # phone-number-here
#         'order[billing_address]':   '123 Seurat lane',                        # your address
#         'order[billing_address_2]': '',
#         'order[billing_zip]':       '90210',                                  # zip code
#         'order[billing_city]':      'Beverly Hills',                          # city
#         'order[billing_state]':     'CA',                                     # state
#         'order[billing_country]':   'USA',                                    # country
#         'store_address':            '1',
#         'credit_card[type]':        'visa',                                   # master or visa
#         'credit_card[cnb]':         '9999 9999 9999 9999',                    # credit card number
#         'credit_card[month]':       '01',                                     # expiration month
#         'credit_card[year]':        '2026',                                   # expiration year
#         'credit_card[vval]':        '123',                                    # cvc/cvv
#         'order[terms]':             '0',
#         'order[terms]':             '1'
#     }
#     requests.get()

supreme(options)
