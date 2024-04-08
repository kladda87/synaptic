from django.db import models

class News(models.Model):
    headline = models.CharField(max_length=100, default='Headline')
    body_text = models.TextField(max_length=10000, default='...')
    date_published = models.DateTimeField(auto_now_add=True)
    news_image = models.ImageField(upload_to='news_images/', null=True, blank=True)

class FAQ(models.Model):
    question = models.CharField(max_length=200, default='Question')
    answer = models.CharField(max_length=200, default='Answer')

class Staff(models.Model):
    name = models.CharField(max_length=100, default='Name')
    title = models.CharField(max_length=100, default='Title')
    description = models.TextField(max_length=2500, default='Description')
    staff_image = models.ImageField(upload_to='staff_images/', null=True, blank=True)

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()