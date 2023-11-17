# build_files.sh
echo "Python version:"
python --version
echo "Pip version:"
pip --version

echo "Installing requirements..."
pip install -r requirements.txt

echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput
echo "Python version:"
python --version