# Django


### 环境初始化

	python3 install virtualenv
	cd demosite
	mkdir py3env
	virtualenv ./py3env/
	source py3env/bin/activate

	#install Django
	pip3 install Django

### 项目初始化

	django-admin startproject demosite
	python manage.py runserver
	python manage.py startapp polls


### 项目结构

	demosite/
		manage.py
		demosite/
			__init__.py
			settings.py
			urls.py
			wsgi.py
		polls/
			__init__.py
			admin.py
			apps.py
			migrations/
				__init__.py
			models.py
			tests.py
			views.py

