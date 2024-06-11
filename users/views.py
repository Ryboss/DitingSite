from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm
from .models import Profile, Like
from django.contrib.auth.models import User

from math import radians

from core.core import send_email, Distance, Watermark
from users.transactions import user_register


def home(request):
    profiles = Profile.objects.all()
    return render(request, 'users/home.html', {'profiles': profiles})


def profiles(request, profile_id):
    profile = Profile.objects.filter(pk=profile_id)

    if request.method == 'POST':
        who_likes = request.user.username
        id_user = request.user.id
        mail = request.user.email

        for p in profile:
            name = p.user

        Like.objects.create(who_likes = who_likes,profile_likes=name, user=id_user)

        if Like.objects.filter(who_likes=name, profile_likes = who_likes):
            message = f'Hello dear friend {who_likes} You mutually like with {name}'
            send_email(message, mail)

    if User.is_authenticated:
        id = request.user.id
        auth_user= Profile.objects.filter(user = id)

        longitude_auth=radians(auth_user.longitude)
        latitude_auth=radians(auth_user.latitude)

        longitude2 = radians(profile.longitude)
        latitude2 = radians(profile.latitude)

        if all([longitude_auth, longitude2, latitude_auth, latitude_auth]):
            distance = Distance(longitude_auth, longitude2, latitude_auth, latitude_auth)

    return render(request,'users/profiles.html', locals())


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            profile = user_register(form)

            messages.success(request, f'Account created for {profile.user.username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = "users/login.html"

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)

            self.request.session.modified = True

        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = """We've emailed you instructions for setting your password,
                      if an account exists with the email you entered. You should receive them shortly.
                      If you don't receive an email,
                      please make sure you've entered the address you registered with, and check your spam folder."""
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


class ProfileView(View):
    form_class = UpdateUserForm
    template_name = "users/profile.html"

    def get(self, request):
        print(request)
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

        return render(request, self.template_name, locals())

    def post(self, request):
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        print(profile_form.is_valid())
        if profile_form.is_valid() and User.is_authenticated:
            if avatar := profile_form.data.get("avatar"):
                w_photo = Watermark(avatar, request.user.id)
                profile_form.avatar = w_photo.watermark_image()
            profile_form.save()

            messages.success(request, 'Изменения успешно сохранены')

            return redirect(to='users-profile')
        messages.success(request, 'Некорректные данные')
        return render(request, self.template_name, locals())


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid() and User.is_authenticated:
            w_photo = Watermark(profile_form.data.get("avatar"), request.user.id)
            profile_form.avatar = w_photo.watermark_image()
            user_form.save()
            profile_form.save()

            messages.success(request, 'Your profile is updated successfully')

            return redirect(to='users-profile')

    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})
