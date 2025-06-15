# Django Example
- Uses `db.sqlite3` local database to store data
- Shows CRUD ops as well as a simple Sqlite3 DB reader.
## Run locally
- Clone the repo to a clean dir. Change working dir to the root dir created by `git clone`. 
- Run `python .\manage.py runserver 8005` (8005 is the port number) from the root dir to use the application locally. You can use any available logical port.
- Before running the app, please run `pip install -r requirements.txt` from a virtual environment.
- A missing package can be installed using `pip install <package_name>`

## Authentication
- Uses basic support for auth using the `django.contrib.auth` and `accounts` apps.
## Sqlite3 Reader
- Reads Sqlite3 Db file which you can point to using file chooser dialog. Accepted file extension is `.sqlit3`.
- Displays all the tables and their data in a grid.
- Create a blank Sqlite3 DB. Run `python manage.py makemigrations` and `python manage.py migrate` as necessary to ensure models are reflected in the Sqlite3 DB.

# Docker support
- Use the `dockerfile` to create an image and a container from the image. This will run the Django app in a container. 
- `docker build -t prasadnarwadkar/djangoapp . --no-cache`
- `docker run --env=PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin --env=GPG_KEY=7169605F62C751356D054A26A821E680E5FA6305 --env=PYTHON_VERSION=3.13.3 --env=PYTHON_SHA256=40f868bcbdeb8149a3149580bb9bfd407b3321cd48f0be631af955ac92c0e041 --network=bridge --workdir=/usr/src/app -p 8003:8000 --restart=no --runtime=runc -d prasadnarwadkar/djangoapp:latest`
