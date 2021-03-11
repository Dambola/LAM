# LAM
## Description
This is a web application for Worship Bands to manage the songs and other things.
LAM means Louvor Agape Montese.

## Team
This is a development of ProjectNogueira - Daniel Nogueira Rebouças

## Language
Python 3.6
Flask for web service and Flask-Restful-Api for api service.
Quasar Framework
Mysql 8.0

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

## Running
### Testing
First install pytest-cov (pip install pytest-cov)

For cmd report:
```
pytest -vv --cov=moppy tests
```

For complex html report (the report will be exported in "htmlcov" folder):
```
pytest -vv --cov=moppy --cov-report=html tests
```

## Code Information:
- Code Covering: 34%

## License
[MIT](https://choosealicense.com/licenses/mit/)