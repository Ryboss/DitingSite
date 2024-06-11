from django.urls import path
from .views import home, profile, RegisterView, profiles, CustomLoginView, ProfileView

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='register'),
    path("login/", CustomLoginView.as_view(), name="login"),
    path('profile/', ProfileView.as_view(), name='users-profile'),
    path('profiles/<int:profile_id>', ProfileView.as_view(), name='profiles')
]
