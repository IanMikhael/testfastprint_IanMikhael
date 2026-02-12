"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path
from app_produk import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.produk_list, name='produk_list'),
    path('tambah/', views.produk_tambah, name='produk_tambah'),
    path('edit/<int:id>/', views.produk_edit, name='produk_edit'),
    path('hapus/<int:id>/', views.produk_hapus, name='produk_hapus'),
]