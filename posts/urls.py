from django.urls import path
from . import views
urlpatterns = [
    path('posts', views.PostsmixinsApi.as_view(), name='post'),
    path('detail/posts/<int:pk>', views.DetailPostMixinApi.as_view(), name='detail'),
    path('comment', views.Commwntmixin.as_view(), name='Add_comment'),
    path('comment/delete/<int:pk>', views.Commwntmixin.as_view(), name='delete_comment'),
]