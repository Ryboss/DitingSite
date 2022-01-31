from django.urls import path
from .views import home, profile, RegisterView, profiles

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('profiles/<int:profile_id>',profiles, name='profiles')
]
