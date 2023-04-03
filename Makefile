#init application
init:
	@python3 -m venv env

#install requirements
install:
	@pip install -r requirements.txt

#run app.py
run:
	@python app.py