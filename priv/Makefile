# Makefile
VENV_NAME = venv
VENV_CMD = python3 -m venv $(VENV_NAME)
ACTIVATE_VENV = source $(VENV_NAME)/bin/activate
INSTALL_REQ = pip install -r requirements.txt

# Create Venv and activate it
venv:
	$(VENV_CMD) && \
	$(ACTIVATE_VENV)

# Target to create the virtual environment and install requirements
install:
	$(INSTALL_REQ)

# Target to clean up
clean:
	rm -rf $(VENV_NAME)

# Set the default target
.DEFAULT_GOAL := install
