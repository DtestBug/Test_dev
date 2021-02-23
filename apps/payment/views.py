from rest_framework import permissions
from rest_framework import mixins
from rest_framework.generics import GenericAPIView

from payment.serializers import PaymentModelSerializer
from payment.models import PaymentModels


class PaymentViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     GenericAPIView
                     ):
    queryset = PaymentModels.objects.all()
    serializer_class = PaymentModelSerializer
    # permission_classes = [permissions.IsAuthenticated]
    ordering_fields = ('id', 'name')

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
