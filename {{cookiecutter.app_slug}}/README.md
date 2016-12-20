# {{cookiecutter.human_name}}

{{cookiecutter.description}}

## Dependencies:
1. https://github.com/kennethreitz/autoenv
2. Install requrements
    ```python
    	virtualenv venv -p python
    	. venv/bin/activate
    	pip install -r requirements.txt
    	
    	# Start the server:
    	flask server
    ```


[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)








# Clone cookiecutter
cookiecutter https://github.com/pgallen90/minimal_flask

# Set up Github repo
curl -F 'login=username' -F 'token=API Token' https://github.com/api/v2/yaml/repos/create -F name=reponame
