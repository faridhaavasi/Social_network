from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post

class PostApi(APIView):
    def get(self,request, pk):
        instance = Post.objects.get(pk=pk)


