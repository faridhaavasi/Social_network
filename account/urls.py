from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/register', views.RegisterView.as_view()),

    path('api/login/', TokenObtainPairView.as_view(), name='login_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='login_refresh'),
]

