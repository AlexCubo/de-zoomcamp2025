### Question 1. 
#### Run docker with the python:3.12.8 image in an interactive mode, use the entrypoint bash. What's the version of pip in the image?

1. $ docker run -it python:3.12.8 bash
2. root@251693c867c5:/# pip --version

Answer: 
```
pip 24.3.1 from /usr/local/lib/python3.12/site-packages/pip
```
### Question 2.
#### Given the following docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?
```
services:
  db:
    container_name: postgres
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: 'postgres'
      POSTGRES_PASSWORD: 'postgres'
      POSTGRES_DB: 'ny_taxi'
    ports:
      - '5433:5432'
    volumes:
      - vol-pgdata:/var/lib/postgresql/data

  pgadmin:
    container_name: pgadmin
    image: dpage/pgadmin4:latest
    environment:
      PGADMIN_DEFAULT_EMAIL: "pgadmin@pgadmin.com"
      PGADMIN_DEFAULT_PASSWORD: "pgadmin"
    ports:
      - "8080:80"
    volumes:
      - vol-pgadmin_data:/var/lib/pgadmin  

volumes:
  vol-pgdata:
    name: vol-pgdata
  vol-pgadmin_data:
    name: vol-pgadmin_data
```
Answer:
```
db:5432
```

### Question 3.
#### During the period of October 1st 2019 (inclusive) and November 1st 2019 (exclusive), how many trips, respectively, happened:
1. Up to 1 mile
2. In between 1 (exclusive) and 3 miles (inclusive),
3. In between 3 (exclusive) and 7 miles (inclusive),
4. In between 7 (exclusive) and 10 miles (inclusive),
5. Over 10 miles

Query:
```
with one as
(select count(index) from green_taxi_data where trip_distance <= 1),
three as
(select count(index) from green_taxi_data where trip_distance > 1 
											and  trip_distance <= 3),
seven as 
(select count(index) from green_taxi_data where trip_distance > 3
											and  trip_distance <= 7),
ten as
(select count(index) from green_taxi_data where trip_distance > 7
											and  trip_distance <= 10),
morethen10 as
(select count(index) from green_taxi_data where trip_distance > 10)
select * from one, three, seven, ten, morethen10;
```
Result:
```
104838	199013	109645	27688	35202
```
### Question 4.
####  Which was the pick up day with the longest trip distance? Use the pick up time for your calculations.

Query:
```
SELECT 
	CAST(lpep_pickup_datetime AS DATE) AS data_max_trip
FROM green_taxi_data
WHERE trip_distance = (SELECT MAX(trip_distance)FROM green_taxi_data);
```
Result:
```
2019-10-31
```

### Question 5.
#### Which were the top pickup locations with over 13,000 in total_amount (across all trips) for 2019-10-18?

Query:
```
WITH top_locations AS
(SELECT td."PULocationID" as "locID", SUM(td."total_amount") as sum_tot_amount
 FROM green_taxi_data td
 WHERE DATE(td."lpep_pickup_datetime") = '2019-10-18'
 GROUP BY 1)
SELECT zl."Zone", tl."locID", tl."sum_tot_amount"
FROM taxi_zone_lookup zl
JOIN top_locations tl
ON tl."locID"=zl."LocationID"
ORDER BY tl."sum_tot_amount" DESC
LIMIT 3;
```
Result:
```
East Harlem North, East Harlem South, Morningside Heights
```

### Question 6.
#### For the passengers picked up in Ocrober 2019 in the zone name "East Harlem North" which was the drop off zone that had the largest tip?
Query:
```
SELECT	zpu."Zone" AS pickup_zone, gtd."PULocationID" AS pickup_id, 
		zdo."Zone" AS dropoff_zone, gtd."DOLocationID" AS dropoff_id,
		gtd."tip_amount"
FROM	taxi_zone_lookup zpu
JOIN	green_taxi_data gtd
ON 		zpu."LocationID" = gtd."PULocationID"
JOIN	taxi_zone_lookup zdo
ON 		zdo."LocationID" = gtd."DOLocationID"
WHERE	zpu."Zone" = 'East Harlem North'
ORDER BY	gtd."tip_amount" DESC
LIMIT 	1;
```
Results:
```
|"pickup_zone"      |"pickup_id"| "dropoff_zone" |"dropoff_id"|"tip_amount"|
|"East Harlem North"|    "74"   |  "JFK Airport" |    "132"   |   "87.3"   |
```
Answer:
```JFK Airport ```

### Question 7
#### Which of the following sequences, respectively, describes the workflow for:
1. Downloading the provider plugins and setting up backend,
2. Generating proposed changes and auto-executing the plan
3. Remove all resources managed by terraform`

Answer:
``` terraform init, terraform apply -auto-approve, terraform destroy ```