import requests
import urllib2
from bs4 import BeautifulSoup
from termcolor import colored


supreme_text = '''
$$$$$$$$$$$$$$$$$       $$$           $$$       $$$$$$$$$$$$$$$$$       $$$$$$$$$$$$$$$$$       $$$$$$$$$$$$$$$$$       $$$$$$   $$$$$$     $$$$$$$$$$$$$$$$$
$$$                     $$$           $$$       $$$           $$$       $$$           $$$       $$$                     $$$ $$$ $$$ $$$     $$$
$$$$$$$$$$$$$$$$$       $$$           $$$       $$$$$$$$$$$$$$$$$       $$$$$$$$$$$$$$$$$       $$$$$$$$$$$$$$$$$       $$$  $$$$   $$$     $$$$$$$$$$$$$$$$$
              $$$       $$$           $$$       $$$                     $$$        $$$          $$$                     $$$         $$$     $$$
$$$$$$$$$$$$$$$$$       $$$$$$$$$$$$$$$$$       $$$                     $$$           $$$       $$$$$$$$$$$$$$$$$       $$$         $$$     $$$$$$$$$$$$$$$$$'''
print colored(supreme_text, 'red')

print '\nChoose a number from the options below'

options = raw_input('\t\tOptions:\n\t\t1 for jackets\n\t\t2 for shirts\n\t\t3 for tops/sweaters\n\t\t4 for sweatshirts\n\t\t5 for pants\n\t\t6 for t-shirts\n\t\t7 for hats\n\t\t8 for bags\n\t\t9 for accessories\n\t\t10 for skate\n\t\t11 for all\nEnter: ')

base_url = 'http://www.supremenewyork.com/shop/'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36'
                '(KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36'}

global product_id
global variant
global page
global product_page
global products
global colors

def supreme(options):
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

    items = []
    color = []
    variants = []

    for products in soup.findAll('h1')[1:]:
        products = products.text
        items.append(products)

    for colors in soup.findAll('p'):
        colors = colors.text
        color.append(colors)

    print '\nProducts: \n'
    for item in items:
        print colored(item + '\n', 'red')
    print 'Colors: \n'
    for colors in color:
        print colored(colors + '\n', 'cyan')
    return items, color

def add_to_cart(item, clr):
    correct_product = False
    correct_color = False

    while not correct_product:
        choose_products = raw_input(colored('Enter in a product from the products above: ', 'yellow'))
        if choose_products not in item:
            print colored('Invalid product!!!', 'red')
        else:
            correct_product = True

    while not correct_color:
        choose_colors = raw_input(colored('Enter in a color from the colors above: ', 'yellow'))
        if choose_colors not in clr:
            print colored('Invalid color!!!', 'red')
        else:
            correct_color = True

item, clr = supreme(options)
add_to_cart(item, clr)
