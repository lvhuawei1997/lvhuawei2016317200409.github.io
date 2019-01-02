"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, re_path
from django.conf.urls import include
from django.contrib import admin
from login import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
    url(r'^captcha', include('captcha.urls')),
    url(r'^land/', views.land),
    url(r'^addland/', views.addland),
    re_path(r"^delland/(\d+)", views.delland),
    re_path(r"^editland/(\d+)", views.editland),
    url(r'^product/', views.product),
    url(r'^addproduct/', views.addproduct),
    re_path(r"^delproduct/(\d+)", views.delproduct),
    re_path(r"^editproduct/(\d+)", views.editproduct),
    url(r'^returnfarmer/', views.returnfarmer),
    url(r'^croprecords/', views.croprecords),
    url(r'^addcroprecords/', views.addcroprecords),
    re_path(r"^delcroprecords/(\d+)", views.delcroprecords),
    re_path(r"^editcroprecords/(\d+)", views.editcroprecords),
    url(r'^recovery/', views.recovery),
    url(r'^addrecovery/', views.addrecovery),
    re_path(r"^delrecovery/(\d+)", views.delrecovery),
    re_path(r"^editrecovery/(\d+)", views.editrecovery),
    url(r'^dosage/', views.dosage),
    url(r'^adddosage/', views.adddosage),
    re_path(r"^deldosage/(\d+)", views.deldosage),
    re_path(r"^editdosage/(\d+)", views.editdosage),
    url(r'^page_not_found', views.page_not_found),

]
handler404 = views.page_not_found
handler500 = views.page_error
