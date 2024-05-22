# Full Stack Django Projects:

### Setup:
virtualenv django_common_env
django_common_env\scripts\activate
pip install django
pip install pygments
celery -A django_celery_redis worker -l info --pool=solo

### Project 1: Film Companion Rest API
1. Lets user register/signup
2. View movie list, description and reviews
3. Add new movies and its details
4. Add reviews
