from django.urls import path
from django.views.generic import TemplateView
from main import views

urlpatterns = [
    # NB: The name argument below allows us to use a function called reverse() 
    # that maps the names to the actual URL paths
    path('', TemplateView.as_view(template_name='home.html'), name="home"),
    path('about-us/', TemplateView.as_view(template_name='about_us.html'), name="about_us"),
    path('contact-us/', views.ContactUsView.as_view(), name='contact_us'),
]