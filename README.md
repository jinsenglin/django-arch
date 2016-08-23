# django-arch

# Setup Development Environment
pip install -r requirements.txt

pip install -r requirements-dev.txt

# Setup Production Environment
pip install -r requirements.txt

# Start Development Server (Prerequisite : Setup Production Environment)
cd mysite && python manage.py runsever

# Run Test (Prerequisite : Setup Development Environment)
cd mysite && pytest -v -n 2 --cov [test suite]

-v means verbose

-n 2 means with 2 parallel processes

--cov means with coverage report

test suite e.g., mysite or app1
