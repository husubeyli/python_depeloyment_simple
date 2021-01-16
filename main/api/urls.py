from django.urls import path, include
from main.api.views import AccountAPIView



urlpatterns = [
    path('account/', AccountAPIView.as_view(), name='account'),

]