"""
URL configuration for ProjectSuppliment project.

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
from django.urls import include
from django.contrib import admin
from django.urls import path
from supplimentApp.views import *
from rest_framework import routers

routers = routers.DefaultRouter()
# routers.register("user-type", UserTypeView, basename="user-type")
routers.register("products", ProductView, basename="product")
routers.register("customers", CustomerView, basename="customer")
routers.register("orders", OrdersView, basename="orders")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(routers.urls)) ,
    path('api/login/', LoginView.as_view(), name='login'),
] 
