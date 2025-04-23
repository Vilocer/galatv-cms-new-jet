# Gala TV - CMS Site Version. Ready to Production!
<div align="center">
  <a href="https://github.com/Vilocer/galatv-cms-new-jet">
    <img width="100" height="100" src="https://sun9-47.userapi.com/Y4wLO8JMVQJ-6n41vmyDm8YQXdgJ3DCfYhwH5Q/qLTJrqDApVM.jpg">
  </a>
  <br>
  <br>
</div>

## Need
- Python >=3.6.2 (recommend python-3.8.5)
- All python packages in requirements.txt

## Installation - Unix
- `git clone https://github.com/Vilocer/galatv-cms-new-jet && cd galatv-cms-new-jet` - Clone repository.
- `python -m venv env && source/env/bin/activate` - Create and activate virtualenv.
- `pip install -r requirements.txt` - Install need python packages.

##  Configuration - Unix
- `chmod +x bin/add_env.sh` - Add run permissions.
- `./bin/add_env.sh` - Run, that script generate .env conf in project directory, you just need to put you values! (example - example.env).

## Run 
- `source env/bin/activate` - Activate virtualenv.
- `python src/manage.py runserver` - Run Default Development Django Web Server.

## Important Files
- `src/config/settings.py` - Django settings.
- `src/config/wsgi.py` - WSGI config for Django.
- `src/config/asgi.py` - ASGI config for Django.

## Also Django-admin commands

- `python src/manage.py migrate` - Run Database migration.
- `python src/manage.py updaterates` - Make a rates drag and drop in admin-panel.
