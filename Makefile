start:
	docker-compose build
	git pull
	docker-compose build
	docker-compose up
