# LAM
## Description
This is a web application for Worship Bands to manage the songs and other things.<br>
LAM means Louvor Agape Montese.

## Team
This is a development of ProjectNogueira - Daniel Nogueira Rebouças

## Language
Python 3.6<br>
Flask for web service and Flask-Restful-Api for api service.<br>
Quasar Framework<br>
Mysql 8.0<br>
Docker

## Main Features
- Manage your bills through a web interface by adding information on expenses or earnings.
- Categorize and perform specific analyzes through a web interface or access to the api.
- Graphical analyzes with customized algorithms. (pluggable graphics)

## Commits Convention
### Types
- feat: When a commit add a new feature or improves an existing one.
- fix: When a commit represents a correction of a problem.
- config: When a commit add or change configurations.
- docs: When a commit add or change documentations.
- refactor: When a commit represents a refactor of the code.
- test: When a commit add or change a testing file/feature.
- revert: When a commit is a reverting operation.
- impl: When a commit is a implementation operation.

### Basic Rule
The first line of the commit message is only made by development information. Inform the commit type and a little description and explain the context of the change (example: controller, model, api, parser, sql).<br>
The optional body is followed by a blank line if it is to be used. You can describe better here the commit information.<br>
The footer is also followed by a blank line if it is to be used.<br>
The footer is used to specify or alert something important. Soo the footer must be only in upper case letters. Just use this when it is really needed.

### Commit format
```
<type>(context): <description>

[optional-body]

[optional-footer]
```

## Installation

### Database
To create a database service, we are using Docker.

```sh
docker run -p 3306:3306 --name MysqlService -e MYSQL_ROOT_PASSWORD=<PASSWORD> -v <CONTAINER_PATH>:/var/lib/mysql -d mysql:8 mysqld --default-authentication-plugin=mysql_native_password
```

### LAM Web Application
To create the Quasar Web Application service, we are using Docker.
Build the image from LAMWeb\Dockerfile.

```sh
sudo docker build -t lam-web .
sudo docker run -p 80:80 -d --name LamWebService lam-web
```

### LAM Rest API
To create the Flask Rest API service, we are using Docker.

```sh

```

## Running
First install pytest-cov (pip install pytest-cov)

### Unit Testing
For cmd report:
```
pytest -vv --cov=lamapi tests
```

For complex html report (the report will be exported in "htmlcov" folder):
```
pytest -vv --cov=lamapi --cov-report=html tests
```

### Integration Testing
First install pytest-cov (pip install pytest-cov)

For cmd report:
```
pytest -vv e2e
```

## Code Information:
- Code Covering: 34%

## License
[MIT](https://choosealicense.com/licenses/mit/)