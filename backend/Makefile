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
	