from django.shortcuts import render, redirect
from .models import Staff, News, FAQ 
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseServerError
import logging
from django.conf import settings
from django.contrib import messages


logger = logging.getLogger(__name__)

def staff(request):
    try:
        staff_members = Staff.objects.all()  # Query the database for all Staff objects
        return render(request, 'main/staff.html', {'staff_members': staff_members})
    except Exception as e:
        logger.error(f"Error in staff view: {str(e)}")
        return HttpResponseServerError("Internal Server Error")

def faq(request):
    try:
        faq_list = FAQ.objects.all()  # Query the database for all Staff objects
        return render(request, 'main/faq.html', {'faq_list': faq_list})
    except Exception as e:
        logger.error(f"Error in faq view: {str(e)}")
        return HttpResponseServerError("Internal Server Error")

def news(request):
    try:
        news_list = News.objects.all().order_by('-date_published')  # Sorting by newest first
        return render(request, 'main/news.html', {'news_list': news_list})
    except Exception as e:
        logger.error(f"Error in news view: {str(e)}")
        return HttpResponseServerError("Internal Server Error")

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def treatments(request):
    return render(request, 'main/treatments.html')

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            # Email data
            user_email = form.cleaned_data.get('email_address')
            subject = "New Contact Message from {}".format(form.cleaned_data.get('first_name'))
            message = form.cleaned_data.get('message')
            admin_email = settings.EMAIL_HOST_USER  # Email defined in settings.py

            # Send email to admin
            send_mail(subject, message, admin_email, [admin_email])

            # Send confirmation email to user
            send_mail("Thank you for contacting us", "We have received your message and will get back to you soon.", admin_email, [user_email])
            user_email = form.cleaned_data.get('email_address')

            return render(request, 'main/contact_success_page.html', {'user_email': user_email})
    else:
        form = ContactForm()

    return render(request, 'main/contact_us.html', {'form': form})

def contact_success_page(request):
    return render(request, 'main/contact_success_page.html')