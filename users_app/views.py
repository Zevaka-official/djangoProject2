import os
import random
import string

from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView

from users_app.forms import UserRegisterForm, UserLoginForm, UserForgotPasswordForm, UserSetNewPasswordForm
from users_app.models import User


class UserLoginView(LoginView):
    """
    Представление авторизация на сайте
    """
    form_class = UserLoginForm
    template_name = 'users_app/login.html'
    next_page = 'main:index'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация на сайте'
        return context


class RegisterView(CreateView):
    """
    Представление регистрации на сайте с формой регистрации
    """
    model = User
    form_class = UserRegisterForm
    template_name = 'users_app/register.html'
    success_url = reverse_lazy('users_app:email_confirmation_sent')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        new_user = form.save()
        # Создаем и сохраняем токен подтверждения
        token = ''.join(random.choices(string.ascii_letters + string.digits, k=25))
        new_user.email_verificator = token
        new_user.save()
        # Отправляем письмо с подтверждением
        current_site = get_current_site(self.request)
        mail_subject = 'Conrirm registration'
        message = render_to_string(
            'users_app/email_check.html',
            {
                'domain': current_site.domain,
                'token': token,
            },
        )
        send_mail(mail_subject, message, os.getenv('EMAIL_HOST_USER'), [new_user.email])
        return response


class EmailConfirmationSentView(TemplateView):
    template_name = 'users_app/email_confirmation_sent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Письмо активации отправлено'
        return context


class VerifyEmailView(View):
    """
    Представление верификации нового пользователя по почте
    """

    def get(self, request, token):
        try:
            user = User.objects.get(email_verificator=token)
            user.is_active = True
            user.save()
            return redirect('users_app:email_confirmed')
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return redirect('users_app:email_confirmation_failed')


class EmailConfirmedView(TemplateView):
    template_name = 'users_app/email_confirmed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ваш электронный адрес активирован'
        return context


class EmailConfirmationFailedView(TemplateView):
    template_name = 'users_app/email_confirmation_failed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ваш электронный адрес не активирован'
        return context


class UserForgotPasswordView(PasswordResetView):
    """
    Представление по сбросу пароля по почте
    """
    form_class = UserForgotPasswordForm
    template_name = 'users_app/user_password_reset.html'
    success_url = reverse_lazy('users_app:password-reset-sent')
    subject_template_name = 'users_app/password_subject_reset_mail.txt'
    email_template_name = 'users_app/password_reset_mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запрос на восстановление пароля'
        return context


class PasswordResetSentView(TemplateView):
    template_name = 'users_app/user_password_reset.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Письмо восстановления отправлено'
        return context


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    """
    Представление установки нового пароля
    """
    form_class = UserSetNewPasswordForm
    template_name = 'users_app/user_password_set_new.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Установить новый пароль'
        return context


class UserProfileView(TemplateView):
    template_name = 'users_app/user_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль пользователя'
        return context
