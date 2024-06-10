from django.urls import path
from .views import log_out, register_view, verify, dashboard, resend_otp

urlpatterns = [
    path('register/', register_view, name='register'),

    path('verify/<mobile>', verify, name='verify'),
    path('verify/resend_otp/<mobile>', resend_otp, name='resend_otp'),
    # path('login/', views.mobile_login, name='mobile_login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', log_out, name='logout'),

]
