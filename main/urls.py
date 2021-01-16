from django.urls import path, include


app_name = 'main'

urlpatterns = [
    path('api-auth/', include('main.api.urls'))
]