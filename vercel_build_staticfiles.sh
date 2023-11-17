# Install Python 3.11.5
yum install -y https://centos6.iuscommunity.org/ius-release.rpm
yum install -y python3.11

# Install pip for Python 3.11
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.11 get-pip.py

# Install project requirements
pip install -r requirements.txt

# Build staticfiles
python3.11 manage.py collectstatic --noinput