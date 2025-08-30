from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView    # DRF class for making custom API endpoints
from rest_framework.response import Response  # To send JSON responses
from rest_framework import status            # For HTTP status codes
from .serializers import UserRegistrationSerializer, UserLoginSerializer

def test(request):
    return JsonResponse({"message": "Accounts API working!"})

class UserRegistrationView(APIView):

    # Handles POST request for user signup
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)  
        # Take incoming JSON and pass into serializer
        
        if serializer.is_valid():  # Check if all fields are valid
            serializer.save()      # Save into users table
            return Response(
                {"Status": 1, "message": "User registered successfully!"},
                status=status.HTTP_201_CREATED
            )
        
        # If invalid, return errors (like "email already exists")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']  # Retrieved from validate()
            return Response(
                {
                    "Status" : 1,
                    "message": "Login successful!",
                    "user": {
                        "id": user.id,
                        "name": user.name,
                        "email": user.email
                    }
                },
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)