from celery import shared_task
import time

@shared_task
def send_post_notification(title):
    # Simulate sending email
    time.sleep(2)
    print(f"📧 Notification: New post created - {title}")
    return f"Notification sent for {title}"
