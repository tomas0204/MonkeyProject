# Install Python 3.11.5
yum install -y https://centos6.iuscommunity.org/ius-release.rpm
yum install -y python3.11

# Install pip for Python 3.11
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install --upgrade pip
# Install project requirements
pip install -r requirements.txt

# Build staticfiles
python manage.py collectstatic --noinput