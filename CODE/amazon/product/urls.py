from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('login', views.login, name = 'login'),
    path('register', views.register, name = 'register'),
    path('fb', views.fb, name = 'fb'),
    path('contact', views.contact, name = 'contact'),
    path('mobile', views.mobile, name = 'mobile'),
    path('laptop', views.laptop, name = 'laptop'),
    path('product', views.product, name = 'product'),
    path('prediction', views.prediction, name = 'prediction'),
    path('amzsearch', views.amzsearch, name='amzsearch'),
    path('result',views.result,name='result'),
    path('forgot-password', views.forgotPassword, name = 'forgot-password'),
    path('update-password', views.updatePassword, name = 'update-password'),
]