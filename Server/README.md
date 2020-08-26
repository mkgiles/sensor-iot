# Server
A Python Dash application for displaying aggregate data to the user
## Setting up
To use this script, you need to have a MySQL database running where the server can access it, preferably on the same machine. There should be a table for each base station within the database. Before preparing to run the application, set the mysql connection string inside the script.
Make sure the appropriate dependencies are installed (the application can be run in development mode by running `python3 app.py`, which will tell you what needs to be installed.)
Once ready, install gunicorn with `pip3 install gunicorn`
## Running the application
To run the application, ensure your user has the privileges to run a server on your desired port, then run `gunicorn app:server` to deploy.
