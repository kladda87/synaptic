from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('treatments/', views.treatments, name='treatments'),
    path('staff/', views.staff, name='staff'),
    path('news/', views.news, name='news'),
    path('faq/', views.faq, name='faq'),
    path('contact_success_page/', views.contact_success_page, name='contact_success_page'),
    path('contact_us/', views.contact_us, name='contact_us'),
]
