from django.urls import path
from home.views import home
from home.views import my_logout

urlpatterns = [
    path('', home, name='home'),
    path('logout/', my_logout, name='logout'),
]
