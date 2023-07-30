from django.urls import path
from . import views
urlpatterns = [
    path('posts', views.PostsmixinsApi.as_view(), name='post'),
    path('detail/posts/<int:pk>', views.DetailPostMixinApi.as_view(), name='detail'),

]