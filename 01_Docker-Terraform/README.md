### Some steps for the week 1

I am using my linux machine (Ubuntu 24.04). Therefore I have not configured the WM in google cloud as suggested by the course.

#### To run postgres database from bash (linux)


$ docker run -it \
 -e POSTGRES_USER="root" \
 -e POSTGRES_PASSWORD="root" \
 -e POSTGRES_DB="ny_taxi" \
 -v $(pwd)/ny_taxi_postgres_data:var/lib/postgres/data \
 -p 5432:5432 \
postgres:13
