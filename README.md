# django-arch

# Setup Development Environment
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Setup Production Environment
pip install -r requirements.txt

# Start Development Server (Prerequisite : Setup Production Environment)
cd mysite && python manage.py runsever

# Run Test (Prerequisite : Setup Development Environment)
cd mysite && pytest -v
