from django.urls import path
from .views import ( custom_login, custom_logout, register_user
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register_user, name='register'),
    path('', custom_login, name='login'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),


    # Include Django's built-in password reset views
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # API URLS
    # path('api/register/', custom_register_api, name='api-register'),
    # path('api/login/', custom_login_api, name='api-login'),
    # path('api/logout/', custom_logout_api, name='api-logout'),
]
