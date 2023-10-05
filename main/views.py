from django.shortcuts import render, redirect
from .models import Staff, News, FAQ 
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseServerError
import logging

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

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            # Send emil to be updated later:
            # subject = "New Contact Message from {}".format(form.cleaned_data.get('first_name'))
            # message = form.cleaned_data.get('message')
            # email_from = form.cleaned_data.get('email_address')
            # recipient_list = ['gleiflandberntsson@gmail.com']  # Replace with your email
            # send_mail(subject, message, email_from, recipient_list)

            return redirect('contact_success_page')
    else:
        form = ContactForm()

    return render(request, 'main/contact_us.html', {'form': form})

def contact_success_page(request):
    return render(request, 'main/contact_success_page.html')