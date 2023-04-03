#init application
init:
	@python3 -m venv env

#install requirements
install:
	@env/bin/pip install -r requirements.txt

#run app.py
run:
	@env/bin/python app.py

#run in silent mode
run-s:
	@env/bin/python app.py -s

#clear all output files
clear:
	@rm -rf output