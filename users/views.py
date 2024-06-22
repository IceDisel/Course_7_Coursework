from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from users.models import User
from users.permissions import IsOwner
from users.serializers import UserSerializer
from users.tasks import send_mail_notification


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [AllowAny]

        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser | IsOwner]

        elif self.action in ['list']:
            permission_classes = [IsAdminUser | IsOwner]

        elif self.action in ['retrieve']:
            permission_classes = [IsAdminUser | IsOwner]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        user = serializer.save()
        send_mail_notification.delay(user.email)
