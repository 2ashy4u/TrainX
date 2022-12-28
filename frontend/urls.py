from django.urls import path
from .views import index

# Creates Urls that links with index.html
urlpatterns = [
    path('', index),
    path('Login', index),
    path('Home', index),
    path('*', index)
]
