# BankScrap
Simple web app for scrap stock stats


## Preparation:

Python Installation is required !

- Crate new folder and new working environment using python/pip.
- Install requirements.txt using pip. `pip install -r requirements.txt`,

- Run Django command `python manage.py makemigrations` to make/prepare migrations,
- Run Django command `python manage.py migrate` to implement migrations,
- Run Django command `python manage.py createsuperuser` and create superuser to can use django admin site,
- Run Cron command `ppython manage.py crontab add` to initial cron task,
- Lastly run App using `python3 manage.py runserver`.