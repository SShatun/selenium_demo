# selenium_demo

####PyTest Selenium demo project.

Start Selenium Hub in Docker:
```
docker-compose up -d
```

Install requirements:
```
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt 
```

Run tests with Selenium Hub:
```
pytest tests/ --hub=localhost --remote=True
```

Run tests with local webdriver:
```
pytest tests/ --headless=True --browser=firefox --env=prod
```


Generate allure report:

```
pytest --alluredir ./alluredir

allure generate ./alluredir
```

To configure environment fill the `config/*.yaml` files.
<br>Example:
```
host: https://localhost

user:
  username: username@email.com
  password: passWord

```