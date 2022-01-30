"""DjangoEcommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from DjangoEcommerceApp import views
from DjangoEcommerceApp import AdminViews
from django.conf.urls.static import static

from backend import settings

urlpatterns = [
    path('', views.adminLogin,name="admin_login"),
    path('demo',views.demoPage),
    path('demoPage',views.demoPageTemplate),
    path('admin_login_process',views.adminLoginProcess,name="admin_login_process"),
    path('admin_logout_process',views.adminLogoutProcess,name="admin_logout_process"),

    # PAGE FOR ADMIN
    path('admin_home',AdminViews.admin_home,name="admin_home"),
    
 
    # #Products
    path('product_create',AdminViews.ProductView.as_view(),name="product_view"),
    path('product_list',AdminViews.ProductListView.as_view(),name="product_list"),
    path('product_edit/<str:product_id>',AdminViews.ProductEdit.as_view(),name="product_edit"),
    path('product_add_stocks/<str:product_id>',AdminViews.ProductAddStocks.as_view(),name="product_add_stocks"),
    path('file_upload',AdminViews.file_upload,name="file_upload"),


]