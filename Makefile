build:
	poetry build
package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 gendiff
install:
	poetry install
test:
	poetry run pytest
selfcheck:
	poetry check
check: selfcheck test lint
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml