from django.contrib import admin
from django.urls import path, include
from home import views


admin.site.site_header = "Noman Hafeez"
admin.site.site_title = "Welcome to Noman Dashboard. How can i help you"
admin.site.index_title = "Hey Welcome !"


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('project', views.project, name='project'),
    path('contact', views.contact, name='contact')
]
