from datetime import datetime,timedelta
import random
import pandas as pd
import configparser
import os, string

dirname = os.path.dirname(__file__)

config = configparser.ConfigParser()
config.read(os.path.join(dirname,'config.ini'),encoding='utf-8')

path_generate_files = eval(config['path']['path_generate_files'])

if not os.path.exists(path_generate_files):
    os.makedirs(path_generate_files)

yesterday = datetime.today() - timedelta(days=1)

NUMS_SHOPS = eval(config['nums_shops']['NUMS_SHOPS'])
CATEGORY = eval(config['category']['CATEGORY'])
ITEMS = eval(config['items']['ITEMS'])

if datetime.today().weekday() != 6:
    for shop,cash in NUMS_SHOPS.items():
        for cash_num in cash:
            d_item = {
            'dt': [yesterday.strftime('%d-%m-%y')]*len(ITEMS),
            'doc_id': [f'{shop}{cash_num}{''.join(random.sample(string.ascii_letters+string.digits,6))}' for i in range(len(ITEMS))],
            'item': [random.choice(list(ITEMS.keys())) for i in range(len(ITEMS))], }

            d_price = {
            'category':  [k for k,v in CATEGORY.items() for i in d_item['item'] if i in v],
            'amount': [random.randint(1,6) for i in range(len(ITEMS))],
            'price': [ITEMS[i] for i in d_item['item'] if i in ITEMS.keys()],
            'discount': [random.randint(0,10) for i in range(len(ITEMS))], }
            d_item.update(d_price)

            df=pd.DataFrame(d_item)
            df.to_csv(os.path.join(path_generate_files,f'{shop}_{cash_num}.csv'),index=False)
