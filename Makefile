.PHONY: init-dev
# Init environment for development.
init-dev:
	@pip install --upgrade pip && \
	pip install --requirement requirements.txt && \
	pre-commit install
.PHONY: pre-commit-run
# Run tools for files from commit.
pre-commit-run:
	@pre-commit run

.PHONY: pre-commit-run-all
# Run tools for all files.
pre-commit-run-all:
	@pre-commit run --all-files

.PHONY: homework-i-run
# run homework.
homework-i-run:
	make c-run

.PHONY: homework-i-purge
# Purge homework.
homework-i-prune:
	@make c-prune

.PHONY: c-run
c-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose up --build

.PHONY: c-stop
c-stop:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose down

.PHONY: c-prune
c-prune:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose down --volumes --remove-orphans --rmi local --timeout 0


#without docker
.PHONY: wd-homework-i-run
wd-homework-i-run:
	@python3 main.py

