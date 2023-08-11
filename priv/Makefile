# Makefile

# Set the name of your virtual environment
VENV_NAME = venv

# Command to create a virtual environment
VENV_CMD = python3 -m venv $(VENV_NAME)

# Activate the virtual environment
ACTIVATE_VENV = source $(VENV_NAME)/bin/activate

# Install requirements from requirements.txt
INSTALL_REQ = pip install -r requirements.txt

# Target to create the virtual environment and install requirements
install:
	$(VENV_CMD) && \
	$(ACTIVATE_VENV) && \
	$(INSTALL_REQ)

# Target to clean up
clean:
	rm -rf $(VENV_NAME)

# Set the default target
.DEFAULT_GOAL := install
