from celery import shared_task
from django.contrib.auth.models import User
from django.template.loader import render_to_string

from .models import Post, Category, PostCategory
import datetime
from django.core.mail import EmailMultiAlternatives

@shared_task
def weekly_news():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(dateCreation__gte=last_week)
    categories = set(posts.values_list('postCategory__name', flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))
    html_content = render_to_string(
        'weekly_mail.html',
        {
            'posts': posts,
            'link': f'http://127.0.0.1:8000',
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email="testforskillfactory@yandex.ru",
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    # today = datetime.datetime.now()
    # last_week = today - datetime.timedelta(days=7)
    # posts = Post.objects.filter(dateCreation__gte=last_week)
    # categories = set(posts.values_list('postCategory__name', flat=True))
    # subscribers = set(Category.objects.filter(name__in=categories).values_list('subscriptions', flat=True))
    #
    # html_content = render_to_string(
    #     'weekly_mail.html',
    #     {
    #         'posts': posts,
    #         'link': f'http://127.0.0.1:8000',
    #     }
    # )
    # msg = EmailMultiAlternatives(
    #     subject='Статьи за неделю',
    #     body='',
    #     from_email="testforskillfactory@yandex.ru",
    #     to=subscribers,
    # )
    #
    # msg.attach_alternative(html_content, 'text/html')
    # msg.send()

@shared_task
def send_notifications(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'http://127.0.0.1:8000/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email="testforskillfactory@yandex.ru",
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()