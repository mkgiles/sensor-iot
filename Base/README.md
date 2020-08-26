# Base Station Script
This script is to be run on the base station computer on the same network as the devices.
# Setting up RabbitMQ
In order to use this script, a copy of rabbitmq needs to be running on the machine.
Follow the instructions at [RabbitMQ](http://rabbitmq.com/download.html) to get set up.
Make sure to add an account which can be used to authenticate the devices with the RabbitMQ server.
Once set up, you can add the server details to each device, including an identifier for the base station.
# Connecting to the DB
Make sure there's a MySQL database running somewhere the base station can access, and add a new table to it named after the base station you're setting up. The command for creating such a table is as follows:
```CREATE TABLE `<base station identifier>` (
    `type` CHAR(5) NOT NULL,
    `time` TIMESTAMP NOT NULL,
    `ppm` DOUBLE NOT NULL,
    UNIQUE KEY `time` (`time`)
    );```

Once set up, add the database credentials to the script.
# Running the script
  Run the script with `python3 base.py` or `python3 base.py <base station identifier>`
