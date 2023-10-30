from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, SetemailSerializer
from rest_framework import status
class Setemail(APIView):
    def post(self, request):
        serializer = SetemailSerializer(data=request.data)
        if serializer.is_valid():
            request.session['email'] = serializer.validated_data['emai']
            return Response({'massage': 'ok'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Settoken(APIView):
    def post(self, request):
        pass

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'massage': 'registered'})
        return Response(serializer.errors)
