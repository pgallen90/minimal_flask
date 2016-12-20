# {{cookiecutter.human_name}}

{{cookiecutter.description}}

## Dependencies:
1. https://github.com/kennethreitz/autoenv
    2. Ensure environment variables are set (see .env)
2. Install requrements
    ```python
        virtualenv venv -p python3
        . venv/bin/activate
        pip install -r requirements.txt
        
        # Start the server:
        flask server
    ```


[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.app_slug}})
