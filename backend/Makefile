ifeq ($(shell test -e '.env' && echo -n yes),yes)
	include .env
endif


# Manually define main variables
ifndef APP_HOST
override APP_HOST = 127.0.0.1
endif

ifndef APP_PORT
override APP_PORT = 8000
endif


ALEMBIC_PATH = app/db/alembic.ini


drun:
	uvicorn app.__main__:app --reload

revision:
	alembic -c $(ALEMBIC_PATH) revision --autogenerate

alembic_upgrade:
	alembic -c $(ALEMBIC_PATH) upgrade heads

alembic_downgrade:
	alembic -c $(ALEMBIC_PATH) downgrade heads

drun_docker:
	docker build --build-arg APP_PORT=$(APP_PORT) -t login_image . \
	&& docker run -dp $(APP_PORT):8000 --name login_container login_image

exec_docker:
	docker exec -it login_container bash

del_docker:
	docker rm -f login_container && docker image rm -f login_image

# del_none: docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
	