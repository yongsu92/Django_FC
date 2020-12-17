from django.urls import path
from . import views

app_name = "fcuser"

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login),
    path('logout/',views.logout),
]
