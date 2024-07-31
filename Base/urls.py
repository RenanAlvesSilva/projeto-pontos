from django.urls import path
from .views import *

urlpatterns = [
    path('', Login, name='Login'),
    path('dashboard',Dashboard, name="dashboard"),
    path('logout', Logout_User, name="Logout"),
]
