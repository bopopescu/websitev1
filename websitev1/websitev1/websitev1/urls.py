"""
Definition of urls for websitev1.
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from programming import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('programming/', include(urls)),

    ]
