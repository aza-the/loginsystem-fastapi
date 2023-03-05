run_docker:
	python3 make_env.py \
	&& docker-compose down \
	&& docker-compose build --no-cache \
	&& docker-compose up -d

del_docker:
	docker-compose down \
	&& docker rm -f loginsystemfastapi_postgres_db_1 loginsystemfastapi_backend_1 \
	&& docker image rm -f loginsystemfastapi_backend \
	&& docker volume rm -f loginsystemfastapi_postgres_data

exec_docker:
	docker exec -it loginsystemfastapi_backend_1 make revision \
	&& docker exec -it loginsystemfastapi_backend_1 make alembic_upgrade

frun_docker:
	python3 make_env.py \
	&& docker-compose down \
	&& docker-compose build --no-cache \
	&& docker-compose up -d \
	&& sleep 2 \
	&& docker exec -it loginsystemfastapi_backend_1 make revision \
	&& docker exec -it loginsystemfastapi_backend_1 make alembic_upgrade

	