"""MainProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin            # django tutorial instruction
from django.urls import path, include       # django tutorial instruction
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# "Switchboard" that allows travel to different pages.  In the MainProject,
# this URL list contains paths that lead to different modules or apps when the
# URL in the browser has the string shown at the end.
#   For example, If a URL is http://www.somewebsite.com/amiibo/
#   Django will look for another list of URLs in urls.py of the Amiibo app.
urlpatterns = [
    path('amiibo/', include('Amiibo.urls')),
    path('admin/', admin.site.urls),
    path('', include('HomePage.urls')),
    path('footy/', include('FootyDemo.urls')),
]

urlpatterns += staticfiles_urlpatterns()