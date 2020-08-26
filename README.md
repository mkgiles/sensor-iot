# IoT service for chemical monitoring of environments

## Purpose
As stated in the title, the purpose of this project is to provide the tools necessary to monitor the chemical composition of air in remote environments, such as in greenhouses. In such environments, one or more monitors can be planted, running the device script from this repository. These devices will report back to a base station on site, which collates all of that data and stores it in a remote database. The server then provides a dashboard where an interested party can select base stations to monitor.
The scripts in this repository are designed to be easily extended to add functionality or change specific expectations. Examples being changing the device script to accomodate different sensors, changing the server script to allow more nuanced drilldowns, or changing both to add actuation, e.g. opening a vent when CO has been above a threshold for too long.

## Using this repository
Each folder corresponds to a different device in the IoT stack. With further explanation for what to install and run in each folder's readme.
* The device folder should be loaded onto a raspberry pi.
* The base folder should be loaded onto the base station computer.
* The server folder should be deployed to a web-facing server, preferably the one running the RDBMS.

## Technologies used
These scripts are written using python3 with the following technologies:
* Pandas - For handling data from the database on the server.
* Dash and Plotly - For creating the dashboard and graphs.
* MySQL - For the RDBMS
* RabbitMQ and Pika - For communication between the base station and the individual devices
* GPIOZero - For establishing the SPI communication with sensors
And for hardware:
* Raspberry Pi - For the remote deployment of sensors
* Laptop - For the base station. Any general purpose computer will suffice here, including another raspberry pi.
* Server - I used a VPS, but technically all of this can be run on one device talking to itself
* MQ-7 Sensor - Also used for testing were the MQ-3 ethyl alcohol sensor and MH-71Z CO2 sensor.
* MCP3001 ADC - More commonly used would be an MCP3008, but any method of ADC is acceptable, including a bespoke SAR.
