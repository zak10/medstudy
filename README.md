# projectx template

## Installation (docker) *recommended
1. [Install Docker](https://docs.docker.com/engine/install/)
2. Install yarn `npm install --global yarn`
3. run backend `docker compose up`
4. run frontend `cd frontend && yarn install && yarn dev:vite`
5. create seed data `docker exec nwo-web-1 (was initially listed as nwo_web_1 and couldn't be found) poetry run python manage.py create_seed_data`
6. Navigate to http://localhost:3000


## Installation (macos)
1. brew install pyenv pyenv-virtualenv
2. pyenv install 3.11.1
3. pyenv global 3.11.1
4. pip install virtualenv
5. pyenv virtualenv 3.11.1 nwo
6. pyenv activate nwo
7. curl -sSL https://install.python-poetry.org | python3 -
8. export PATH="~/.local/bin:$PATH" to profile
9. export PYTHONPATH="$PYTHONPATH:~/code/template/src"
8. poetry install


MK Notes when installing
1.need to install python, django, yarn, brew, pip
- brew: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
- python: `brew install python`
- pip: `python -m pip install --upgrade pip`
- django: `pip install django`
- yarn: `brew install yarn`

2.Initializing github repo 
- `git init`
- `git remote add origin https://github.com/zak10/nwo.git`
- `git pull origin main`

3.`yarn cache clean` then `yarn install` in frontend folder (you can navigate with `cd frontend` to go to frontend folder, `cd ..` to go up a folder)

4.`brew install pyenv-virtualenv`

5.needed to run `"export PATH="$HOME/.local/bin:$PATH"` instead of what is stated in #8 above

6.updated docker-compose.yaml   env_file: - frontend/.env/local (was previous looking for .env)

7.`pip3 install django-allauth` needed

8.`pip3 install dj-database-url` needed 

9.`pip3 install dj-database-url` needed 

10.`pip3 install django-ninja-extra` needed