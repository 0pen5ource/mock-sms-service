

build:
	docker build . -t dockerhub/sms-service

run:
	docker run -p 8765:8765 dockerhub/sms-service