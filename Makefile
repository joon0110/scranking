SRC = scranking
SETUP = setup.py
TESTS = scranking/test/*

#########
# BUILD #
#########
develop:  ## install dependencies and build library
	python3 -m pip install -e .[develop]

build:  ## build the python library
	python3 $(SETUP) build build_ext --inplace

install:  ## install library
	python3 -m pip install .

#########
# LINTS #
#########
lint:  ## run static analysis with flake8
	python3 -m black --check $(SRC) $(SETUP)
	python3 -m flake8 $(SRC) $(SETUP)

# Alias
lints: lint

format:  ## run autoformatting with black
	python3 -m black $(SRC)/ $(SETUP)

# alias
fix: format

check:  ## check assets for packaging
	check-manifest -v

# Alias
checks: check

annotate:  ## run type checking
	python3 -m mypy ./$(SRC)

#########
# TESTS #
#########
test: ## clean and run unit tests
	python3 -m pytest -v $(TESTS)

coverage:  ## clean and run unit tests with coverage
	python3 -m pytest -v $(TESTS) --cov=$(SRC) --cov-branch --cov-fail-under=70 --cov-report term-missing

# Alias
tests: test

###########
# VERSION #
###########
show-version:
	bump2version --dry-run --allow-dirty $(SETUP) --list | grep current | awk -F= '{print $2}'

patch:
	bump2version patch

minor:
	bump2version minor

major:
	bump2version major

########
# DIST #
########
dist-build:  # Build python dist
	python $(SETUP) sdist bdist_wheel

dist-check:
	python -m twine check dist/*

dist: clean build dist-build dist-check  ## Build dists

publish:  # Upload python assets
	echo "would usually run python -m twine upload dist/* --skip-existing"

#########
# CLEAN #
#########
deep-clean: ## clean everything from the repository
	git clean -fdx

clean: ## clean the repository
	rm -rf .coverage coverage cover htmlcov logs build dist *.egg-info .pytest_cache

############################################################################################

# Thanks to Francoise at marmelab.com for this
.DEFAULT_GOAL := help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

print-%:
	@echo '$*=$($*)'

.PHONY: develop build install lint lints format fix check checks annotate test coverage show-coverage tests show-version patch minor major dist-build dist-check dist publish deep-clean clean help
