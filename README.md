README.md

Sharded Database with MaxScale and Docker

Project Overview

This project sets up a sharded MariaDB database system using Docker Compose and MariaDB MaxScale as a database proxy/router. It demonstrates basic database sharding by distributing data across two separate master databases (shards) and routing queries to them through MaxScale.

A Python script is provided to connect to the MaxScale instance and perform queries to retrieve and display specific information from the sharded databases.

Project Structure

├── docker-compose.yml
├── maxscale.cnf.d/
│   └── example.cnf
├── sql/
│   ├── master/
│   │   └── init.sql (if applicable)
│   └── master2/
│       └── init.sql (if applicable)
├── query_script.py
├── README.md

Components

docker-compose.yml

Deploys two MariaDB master containers (master, master2)

Deploys one MaxScale container

Mounts config files and exposes ports

MaxScale Configuration (maxscale.cnf.d/example.cnf)

Defines two database servers: zip_master_one and zip_master_two

Configures a schemarouter service (Sharded-Service) to route queries based on database names to the correct shard

Includes a monitor to keep track of both servers' availability

Python Script (query_script.py)

Connects to MaxScale on port 4000

Runs four queries:

Largest zipcode in zipcodes_one

All zipcodes where state is KY

All zipcodes between 40000 and 41000

TotalWages where state is PA from zipcodes_two

Displays query results in the console

How to Run

Clone the repo (or download project files)

Build and run the containers

docker-compose build
docker-compose up -d

Check MaxScale server status

docker-compose exec maxscale maxctrl list servers

Run the Python query script

python3 query_script.py

Expected Output

Example console output:

Largest zipcode in zipcodes_one:
('99999',)

All zipcodes where State='KY':
('40003',)
('40004',)

All zipcodes between 40000 and 41000:
('40001',)
('40002',)

TotalWages where State='PA':
(45000,)
(52000,)

📌 Objectives Accomplished

✅ Set up a sharded database architecture using two MariaDB master instances✅ Configured MaxScale to connect and route queries to both shards via a schemarouter service✅ Developed a Python script to perform database queries through MaxScale✅ Packaged the entire system using Docker Compose✅ Documented the project clearly in this README
