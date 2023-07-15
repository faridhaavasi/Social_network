from django.urls import path
from . import views
urlpatterns = [
    path('detail/<int:pk>', views.PostApi.as_view(), name='detail'),
    path('add_post', views.PostApi.as_view(), name='add_post'),

]