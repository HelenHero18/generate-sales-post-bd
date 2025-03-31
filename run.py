from datetime import datetime,timedelta
import pandas as pd
import configparser
import os
from pgdb import PGDatabase

dirname = os.path.dirname(__file__)

config = configparser.ConfigParser()
config.read(os.path.join(dirname,'config.ini'),encoding='utf-8')

path_generate_files = eval(config['path']['path_generate_files'])
ITEMS = eval(config['items']['ITEMS'])
DATABASE_CREDS = config['database']

database = PGDatabase(
    host = DATABASE_CREDS['HOST'],
    database = DATABASE_CREDS['DATABASE'],
    user = DATABASE_CREDS['USER'],
    password = DATABASE_CREDS['PASSWORD'])

for item,price in ITEMS.items():
    query = """INSERT INTO products (
            item,
            price)
            VALUES (%s,%s)"""
    args = (item,price)
    database.post(query=query,args=args)
    

for file in os.listdir(path_generate_files):
    if 'csv' not in file:
        continue
    df = pd.read_csv(os.path.join(path_generate_files ,file))
    for i,row in df.iterrows():
        query = """INSERT INTO sales (
            dt,
            doc_id,
            item,
            category,
            amount,
            price,
            discount) 
            VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        args = (row['dt'],row['doc_id'],row['item'],row['category'],row['amount'],row['price'],row['discount'])
        database.post(query=query,args=args)
        
database.close_bd()