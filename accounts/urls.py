from django.urls import path 
from .views import RegisterView

# Defines the URL pattern for the user registration API.
# When a POST request is sent to "register/", it calls RegisterView
# to validate the registration data and create a new user.
urlpatterns = [
    path ("register/", RegisterView.as_view(), name= "register" ),
]