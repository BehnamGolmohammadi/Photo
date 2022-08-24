from django.urls import path, include, reverse_lazy
from accounts.views import *
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login', accounts_login, name= 'login'),
    path('logout', accounts_logout, name= 'logout'),
    path('signup', accounts_signup, name = 'signup'),

    path(
        'reset_password',
        auth_views.PasswordResetView.as_view(
            success_url = reverse_lazy('accounts:password_reset_done'),
            template_name = 'registration/password_reset.html',
            subject_template_name = 'registration/password_reset_subject.txt'
            ),
        name = 'reset_password'
        ),
    path(
        'password_reset_done',
        auth_views.PasswordResetDoneView.as_view(),
        name = 'password_reset_done'
        ),
    path(
        'password_reset_confirm/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(success_url = reverse_lazy('accounts:password_reset_complete')),
        name = 'password_reset_confirm'
        ),
    path(
        'password_reset_complete',
    auth_views.PasswordResetCompleteView.as_view(),
    name = 'password_reset_complete'
    ),
]