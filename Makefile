run-docker:
	@docker compose up -d
db-create:
	@poetry run ./ame_data_engineer_challenge/create_tables.py create
db-delete:
	@poetry run ./ame_data_engineer_challenge/create_tables.py delete
