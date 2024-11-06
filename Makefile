# Makefile for ReadyAPI documentation setup

# Define environment and script paths
VENV_DIR = .venv
SCRIPTS_DIR = scripts
DOCS_DIR = docs
MKDOCS = mkdocs
PYTHON = python

# Setup the virtual environment and install requirements
venv:
	@echo "Setting up the virtual environment..."
	python3 -m venv $(VENV_DIR)
	@echo "Activating virtual environment..."
	. $(VENV_DIR)/bin/activate && pip install -r ./requirements/requirements.txt

# Format the code using the provided script
format:
	@echo "Formatting code..."
	bash $(SCRIPTS_DIR)/format.sh

# Run tests with coverage and generate HTML report
test:
	@echo "Running tests and generating coverage report..."
	bash $(SCRIPTS_DIR)/test-cov-html.sh

# Serve documentation live with MkDocs
docs-live:
	@echo "Serving documentation live..."
	$(PYTHON) $(SCRIPTS_DIR)/docs.py live

# Build documentation for all languages
docs-build-all:
	@echo "Building docs for all languages..."
	$(PYTHON) $(SCRIPTS_DIR)/docs.py build-all

# Serve the built documentation
docs-serve:
	@echo "Serving built documentation..."
	$(PYTHON) $(SCRIPTS_DIR)/docs.py serve

# Generate new translation directory for a language
docs-new-lang:
	@echo "Generating new language translation..."
	$(PYTHON) $(SCRIPTS_DIR)/docs.py new-lang $(LANG)

# Live serve docs for a specific language
docs-live-lang:
	@echo "Serving documentation live for $(LANG) language..."
	$(PYTHON) $(SCRIPTS_DIR)/docs.py live $(LANG)

# Install Cligenius CLI and set up completion
cligenius-setup:
	@echo "Setting up Cligenius CLI..."
	cligenius --install-completion

.PHONY: venv format test docs-live docs-build-all docs-serve docs-new-lang docs-live-lang cligenius-setup
