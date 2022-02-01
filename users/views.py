from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required
from PIL import Image, ImageDraw, ImageFont
from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm
from .models import Profile, Like
from django.contrib.auth.models import User
from random import randint
from math import sin, cos, sqrt, atan2, radians, trunc
import smtplib
import email.message


def home(request):
    profiles = Profile.objects.all
    return render(request, 'users/home.html',{'profiles':profiles})


def profiles(request, profile_id):
    global longitude2, longitude_auth, latitude2, latitude_auth
    profile = Profile.objects.filter(pk=profile_id)
    if request.method == 'POST':
        who_likes = request.user.username
        id_user = request.user.id
        mail = request.user.email
        print(mail)
        for p in profile:
            name = p.user
        Like.objects.create(who_likes = who_likes,profile_likes=name, user=id_user)
        if Like.objects.filter(who_likes=name, profile_likes = who_likes):
            email_content = f'Hello dear friend {who_likes} You mutually like with {name}'

            msg = email.message.Message()
            msg['From'] = 'Your gmail'
            msg['To'] = mail
            password = 'Your password'
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(email_content)

            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()

            # Login Credentials for sending the mail
            s.login(msg['From'], password)

            s.sendmail(msg['From'], [msg['To']], msg.as_string())
#Distance
    if User.is_authenticated:
#Radius of Earth in km
        R = 6373.0
        id = request.user.id
        auth_user= Profile.objects.filter(user = id)
        for p in auth_user:
            longitude_auth=radians(p.longitude)
            latitude_auth=radians(p.latitude)
        for p in profile:
            longitude2 = radians(p.longitude)
            latitude2=radians(p.latitude)
        dlon = longitude2-longitude_auth
        dlat= latitude2-latitude_auth
        a=sin(dlat / 2)**2 + cos(latitude_auth) * cos(latitude2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance= trunc(R*c)

    return render(request,'users/profiles.html',{'profile':profile,'distance':distance})


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
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            photo = profile_form.cleaned_data.get('avatar')
            # Create an Image Object from an Image
            im = Image.open(photo)
            width, height = im.size

            draw = ImageDraw.Draw(im)
            text = "watermark"

            font = ImageFont.truetype('arial.ttf', 36)
            textwidth, textheight = draw.textsize(text, font)

            # calculate the x,y coordinates of the text
            margin = 10
            x = width - textwidth - margin
            y = height - textheight - margin

            # draw watermark in the bottom right corner
            draw.text((x, y), text, font=font)
            i = randint(1,10000)
            # Save watermarked image
            im.save(f'media/watermark_images/{i}watermarkimage.jpg')
            user_form.save()
            profile_form.save()
            if User.is_authenticated:
                id = request.user.id
                auth_user = Profile.objects.get(id=id)
                auth_user.avatar = f'watermark_images/{i}watermarkimage.jpg'
                auth_user.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')

    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})
