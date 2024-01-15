# django_projects

django_projects

virtualenv django_common_env
django_common_env\scripts\activate

pip install django
pip install pygments

celery -A django_celery_redis worker -l info --pool=solo
