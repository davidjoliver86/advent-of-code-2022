all: lint test clean

lint:
	black .
	isort . --check
	pylint ./aoc2022 ./tests

test:
	pytest tests/ --cov=aoc2022 --cov-report=term-missing --cov-fail-under=100

clean:
	find . -name "__pycache__" -type d | xargs rm -rf
	find . -name ".pytest_cache" -type d | xargs rm -rf
