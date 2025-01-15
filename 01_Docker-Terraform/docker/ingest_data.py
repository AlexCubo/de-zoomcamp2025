#!/usr/bin/env python
# coding: utf-8

import os
import argparse
import pandas as pd
from sqlalchemy import create_engine
from time import time


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name

    green_data = './data/green_tripdata_2019-10.csv'
    zone_lookup = './data/taxi_zone_lookup.csv'

    # Connection to postgres
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    engine.connect()

    #load taxi lookup data
    zone_lookup_df = pd.read_csv(zone_lookup)
    zone_lookup_df.head(n=0).to_sql(name='taxi_zone_lookup', con=engine, if_exists='replace')
    zone_lookup_df.to_sql(name='taxi_zone_lookup', con=engine, if_exists='replace')

    # load green data
    df_iter = pd.read_csv(green_data, iterator=True, chunksize=100000)

    df = next(df_iter)

    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    df.to_sql(name=table_name, con=engine, if_exists='append')

    try:
        i=0
        while True:

            t_start = time()
            df = next(df_iter)
            i+=1

            df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
            df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

            df.to_sql(name=table_name, con=engine, if_exists='append')
            t_end = time()

            print(f'Inserted Chunk number {i}, took {t_end - t_start}')

    except StopIteration:
        print(f'All Chunks of data ingested into postgres database.')  

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Ingest CSV ny taxi data')

    # user, password, host,database, port, table
    # url of csv files
    parser.add_argument('--user', help='username for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--db', help='database in postgres')
    parser.add_argument('--port', help='postgres port')
    parser.add_argument('--table_name', help='name of the table')

    args = parser.parse_args()
    
    main(args)
