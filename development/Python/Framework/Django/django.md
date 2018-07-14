# Django


### 环境初始化

	python3 install virtualenv
	cd ccops
	mkdir py3env
	virtualenv ./py3env/
	source py3env/bin/activate

	#install Django
	pip3 install Django

### 项目初始化

	django-admin startproject ccops
	python manage.py runserver


### 项目结构

	ccops/
		manage.py
		ccops/
			__init__.py
			settings.py
			urls.py
			wsgi.py