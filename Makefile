all: test

test: fake_test_target
	PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider --cov-report term-missing --cov-branch --cov=. tests/

format:
	black .

.PHONY: fake_test_target
