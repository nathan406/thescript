set -o errexit

pip install -r reuirements.txt

python manage.py collectstatic 
python manage.py migrate