from django.contrib import admin
from django.urls import path, include
from account import views
from . import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('account.urls')),
                
                  path('api/post/', include('posts.urls')),
                  # YOUR PATTERNS
                  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
                  # Optional UI:
                  path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                  path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
