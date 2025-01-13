### Some steps for the week 1

I am using my linux machine (Ubuntu 24.04). Therefore I have not configured the WM in google cloud as suggested by the course.

#### Run postgres database from bash (linux)

$ docker run -it \
 -e POSTGRES_USER="root" \
 -e POSTGRES_PASSWORD="root" \
 -e POSTGRES_DB="ny_taxi" \
 -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgres/data \
 -p 5432:5432 \
 postgres:13

#### Access postgres database

$ pgcli -h localhost -p 5432 -u root -d ny_taxi

#### Run pgAdmin from bash (linux)

1. Create a network to make pgAmin container 
to communicate with postgres container:

$ docker network create pg-network

2. Connect to postgres indicating the network and the name that will
   be used by pgAdmin to connect to postgres:

$ docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v /media/alessandro/Data/Learning/Courses/DE-Zoomcamp_2025/de-zoomcamp2025/01_Docker-Terraform/docker/ny_taxi_postgres_data:/var/lib/postgres/data \
    -p 5432:5432 \
    --network=pg-network \
    --name pg-database \
 postgres:13

 3. Run pgAdmin:

$ docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    --network=pg-network \
    --name pgadmin \
  dpage/pgadmin4  

4. Paste on the browser *localhost:8080* and insert 
the credentials (email and password)  

5. Register to the postgres server
    (see tutorial "DE Zoomcamp 1.2.3 - Connecting pgAdmin and Postgres")