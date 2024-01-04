
# Q-4: What is Django URLs? make program to create django urls.

# ans:

# Django URLs is:

# Django also provides a way to navigate around the different pages in a website.
# When a user requests a URL, Django decides which view it will send it to.
# This is done in a file called urls.py.

# make program to create django urls:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # add more URL patterns as needed
]
