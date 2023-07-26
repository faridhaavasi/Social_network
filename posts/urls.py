from django.urls import path
from . import views
urlpatterns = [
    path('detail/<int:pk>', views.DetailPostApi.as_view(), name='detail'),
    path('posts', views.PostApi.as_view(), name='posts'),

]