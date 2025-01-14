#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
from time import time

# Connection to postgres
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

engine.connect()

df_iter = pd.read_csv('./data/green_tripdata_2019-10.csv', iterator=True, chunksize=100000)

df = next(df_iter)

df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

df.head(n=0).to_sql(name='green_taxi_data', con=engine, if_exists='replace')

df.to_sql(name='green_taxi_data', con=engine, if_exists='append')

try:
    i=0
    while True:

        t_start = time()
        df = next(df_iter)
        i+=1

        df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
        df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

        df.to_sql(name='green_taxi_data', con=engine, if_exists='append')
        t_end = time()

        print(f'Inserted Chunk number {i}, took {t_end - t_start}')

except StopIteration:
    print(f'All Chunks of data ingested into postgres database.')


#Load zone_lookup table

zone_lookup_df = pd.read_csv('./data/taxi_zone_lookup.csv')

df.head(n=0).to_sql(name='taxi_zone_lookup', con=engine, if_exists='replace')

zone_lookup_df.to_sql(name='taxi_zone_lookup', con=engine, if_exists='replace')