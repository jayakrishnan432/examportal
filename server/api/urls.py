from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
app_name = 'api'
urlpatterns = [
    path('token/', obtain_auth_token, name="login"),
    path('', include(router.urls)),
]
