set - o errexit
pip install -r requirement.txt

python manage.py collectstatic --input

python manage.py migrate

if[[$CREATE_SUPERUSER]];
then python manage.py craete superuser --no-input

fi