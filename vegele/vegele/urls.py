"""
URL configuration for vegele project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from WebApp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('receipes/',views.receipe),
    path('index/',views.index),
    path('delete/<slug>',views.delete_receipe),
    path('update/<slug>',views.update_receipe),
    path('login/',views.login_page),
    path('register/',views.register),
    path('logout/',views.logout_page),
]

handler404='WebApp.views.errorhandle'

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
