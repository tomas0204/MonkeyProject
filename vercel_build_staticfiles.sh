# build_files.sh
echo "Python version:"
python --version
echo "Pip version:"
pip --version

echo "Installing requirements..."
pip install -r requirements.txt

echo "Collecting static files..."
python3 manage.py collectstatic --noinput