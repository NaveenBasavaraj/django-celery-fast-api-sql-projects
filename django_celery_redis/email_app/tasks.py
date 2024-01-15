from celery import shared_task
from email_app.email import send_review_email
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@shared_task(name="send_review_email_task")
def send_review_email_task(name, email, review):
    """sends an email when feedback form is filled successfully"""
    logger.info("Sent review email")
    return send_review_email(name, email, review)
