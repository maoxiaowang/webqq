from django.urls import path
from identity.views import account

app_name = 'identity'

urlpatterns = [
    path('register/', account.Register.as_view(), name='register'),
    path('login/', account.Login.as_view(), name='login'),
]
