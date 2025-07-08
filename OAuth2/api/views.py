from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class ExampleApiView(APIView):
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]

    def get(self, request):
        return Response({"message": "GET request - You have read access!"})

    def post(self, request):
        return Response({"message": "POST request - You have write access!"})

class ReadScopeOnlyView(APIView):
    permission_classes = [IsAuthenticated, TokenHasScope]
    required_scopes = ['read']

    def get(self, request):
        return Response({"message": "This endpoint requires read scope only."}, status=status.HTTP_200_OK)
    
from django.http import HttpResponse

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')