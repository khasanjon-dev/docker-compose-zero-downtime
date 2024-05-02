### Env variables
```bash
# WEB
# DEBUG must be empty in production
DEBUG=
SECRET_KEY=django-insecure
DJANGO_SETTINGS_MODULE=root.settings

# DATABASE
DB_HOST=db
DB_NAME=news
DB_USERNAME=postgres
DB_PASSWORD=solve_the_problem
DB_PORT=5432

# POSTGRES
POSTGRES_USER=postgres
POSTGRES_PASSWORD=solve_the_problem
POSTGRES_DB=news
```

# Run the project

> step 1:
- **clone the project**
```shell
git clone https://github.com/khasanjon-dev/nginx-load-balancer-least-conn.git
```
> step 2
- **cd project file**
```shell
cd nginx-load-balancer-least-conn
```
> step 3
```shell
docker compose up --build
```

> step 4 
- **open the new terminal and run this command for testing**
```shell
python test.py
```

# Technologies used

<p>
  <a>
    <img src="https://skillicons.dev/icons?i=python,django,docker,postgres,nginx" />
  </a>
</p>

* ```Python```
* ```Django```
* ```DjangoRestFramework```
* ```Docker```
* ```docker compose```
* ```PostgreSQL```
* ```Nginx```
