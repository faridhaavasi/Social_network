from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import Postserializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins

# region cbv
# class PostApi(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self, request):
#         queryset = Post.objects.all()
#         serializer = Postserializer(instance=queryset, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = Postserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.validated_data['user'] = request.user
#             serializer.save()
#             return Response({'massage': 'added'})
#         return Response(serializer.errors)
#     def delete(self, request, pk):
#         instance = Post.objects.get(pk=pk)
#         instance.delete()
#         return Response({'massage': 'deleted'})
#
#
# class DetailPostApi(APIView):
#     def get(self, request, pk):
#         instance = Post.objects.get(pk=pk)
#         serializer = Postserializer(instance=instance)
#         return Response(serializer.data)
#
# endregion

'''
Create, update and delete operations are implemented by mixins
'''


# region mixin
class PostsmixinsApi(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class DetailPostMixinApi(mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()

    serializer_class = Postserializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

# endregion
