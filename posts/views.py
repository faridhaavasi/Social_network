from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import Postserializer
from rest_framework.permissions import IsAuthenticated
class PostApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        instance = Post.objects.get(pk=pk)
        serializer = Postserializer(instance=instance)
        return Response(serializer.data)
    def post(self, request):
        serializer = Postserializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user'] = request.user
            serializer.save()
            return Response({'massage': 'added'})
        return Response(serializer.errors)


