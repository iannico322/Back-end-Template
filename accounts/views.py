from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .serializers import UserCreateSerializer
from .permissions import IsAccLevelAdmin

User = get_user_model()

class UserDetailView(APIView):
    """
    View to get a user's details in the system using their ID.

    * This view is accessible to anyone.
    """

    def get(self, request, id=None, format=None):
        """
        Return the details of a user.
        """
        try:
            user = User.objects.get(id=id)
            serializer = UserCreateSerializer(user)
            user_data = serializer.data
            office_name = user.office.name
            response_data = f"{user_data['first_name'].capitalize()} {user_data['last_name'].capitalize()} | {user_data['position']} |  {office_name}"
            return Response({"detail": response_data})
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)


class ListUsersView(APIView):
    """
    List/create users (no id in the URL, see accounts/urls.py `all/`) and
    update/delete a specific user (id in the URL, see `update/<id>/`).

    * Restricted to acc_lvl == 0 admins (or Django superusers).
    """
    permission_classes = [IsAccLevelAdmin]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        users = User.objects.all().order_by('id')
        serializer = UserCreateSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create a new user. Password strength is validated on the raw
        password by the serializer; djoser's UserCreateSerializer hashes it
        via create_user() when saving.
        """
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        """
        Update a user.
        """
        user = get_object_or_404(User, id=id)
        serializer = UserCreateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            # Validate the raw password above, then hash it before saving —
            # ModelSerializer.update() doesn't call set_password() on its own.
            password = serializer.validated_data.get('password')
            if password:
                serializer.validated_data['password'] = make_password(password)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, format=None):
        """
        Delete a user.
        """
        if request.user.id == id:
            return Response(
                {"detail": "You cannot delete your own account."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = get_object_or_404(User, id=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
