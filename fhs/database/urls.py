"""fhs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [

    path('login', views.loginpage, name="login"),
    path('about', views.aboutpage, name="about"),
    path('contact', views.contactpage, name="contact"),
    path('', views.indexpage, name="index"),
    path('menu', views.menupage, name="menu"),
    path('hotel', views.hotelpage, name="hotel"),
    path('news-detail', views.newsdetailpage, name="news-detail"),
    path('signupcheck',views.signupcheck,name="signup"),
    path('signincheck',views.signincheck,name="signin"),
    path('forgotpass',views.forgotpass,name='forgotpass'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
    path('verifyotp',views.otp_verify),
    path('newpass',views.newpassfun,name='newpass'),
    path('passsuccess',views.success),
    path('cart',views.get_cart,name='cart'),
    path('empchangepwd', views.empchangepwd, name="empchangepwd"),
    path('empupdatepwd', views.empupdatepwd, name="empupdatepwd"),
    path('changepassword',views.change_password),
    path('signout',views.signout),
path('leave_message',views.leave_message,name="leave_message"),
    path('addcartfun',views.add_cart,name="addcartfun"),
    path('cart/',views.get_cart,name="getcart"),
path("deletecartproduct/<int:uid>",views.deletecartproduct,name="deletecartproduct"),

    path("clearcartafterpayment",views.clearcartafterpayment,name="clearcartafterpayment")
]
