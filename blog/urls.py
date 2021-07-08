from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register),
    path('', login_view),
    path('home/', home),
    path('logout/', logout_view),
]