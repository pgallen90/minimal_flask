# {{cookiecutter.app_slug}}

{{cookiecutter.description}}

## Before Installing:
1. Set environment variables (path to your db, etc).
2. Set environment variables (see /.env)
    1. [Use Autoenv](https://github.com/kennethreitz/autoenv)
    2. Or do it manually ```export VAR="foo"```


## Installing
```
virtualenv venv -p python3;
. venv/bin/activate;
pip install -r requirements.txt;
flask db upgrade;
flask seed;
flask run;
```

## Running the server & scripts:
 * Using Factory Functions best practices based on the [Flask CLI guide](http://flask.pocoo.org/docs/0.12/cli/#factory-functions)

## Deployment to Heroku
This is a shortcut to deploy the app to Heroku from 
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.app_slug}})
