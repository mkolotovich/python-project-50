build:
	poetry build
package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 gendiff
install:
	poetry install
check: selfcheck test lint
test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml