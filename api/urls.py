
from django.urls import path
from .views import UserView

# Home API
urlpatterns = [
    path('user', UserView.as_view())
]
