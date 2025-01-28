
## Module 2

## Kestra
* We are using the gree and yellow taxi data from January 2019 to July 2021. Please upload all the needed data into gcs and bigQuery before to solve the quizes.

### Question 1. 
#### Within the execution for Yellow Taxi data for the year 2020 and month 12: what is the uncompressed file size (i.e. the output file yellow_tripdata_2020-12.csv of the extract task)?

1. $ docker run -it python:3.12.8 bash
2. root@251693c867c5:/# pip --version

Result: 
```
pip 24.3.1 from /usr/local/lib/python3.12/site-packages/pip
```
Answer:
```24.3.1 ```

### Question 2.
#### Given the following docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?



### Question 3.
#### How many rows are there for the Yellow Taxi data for all CSV files in the year 2020?

Query in biqQuery:  
```
SELECT
  COUNT(1)
FROM
  `de-zoomcamp2025.dezc2025_bq_dataset.yellow_tripdata`
WHERE filename LIKE '%2020%';
```
Result:  
~~13,537.299~~
<span style="color: red;">24,648,499</span>
~~18,324,219~~
~~29,430,127~~


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
Answer:
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
Answer:
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
Answer:
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

## Terraform

### Question 7
#### Which of the following sequences, respectively, describes the workflow for:
1. Downloading the provider plugins and setting up backend,
2. Generating proposed changes and auto-executing the plan
3. Remove all resources managed by terraform`

Answer:
``` terraform init, terraform apply -auto-approve, terraform destroy ```