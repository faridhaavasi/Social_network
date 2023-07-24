from django.contrib import admin
from django.urls import path, include
from account import views
from . import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/register', views.RegisterView.as_view()),
                  path('api/login/', TokenObtainPairView.as_view(), name='login_pair'),
                  path('api/login/refresh/', TokenRefreshView.as_view(), name='login_refresh'),
                  path('api/post/', include('posts.urls')),
                  # YOUR PATTERNS
                  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
                  # Optional UI:
                  path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                  path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
