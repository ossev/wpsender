req:
	pip freeze > requirements.txt

send:
	py wps_to_drivers.py

venv:
	venv\Scripts\activate