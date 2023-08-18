from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import PerevalAdded
from .serializers import PerevalAddedSerializer, PerevalAddedDetailSerializer


class SubmitData(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 generics.GenericAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__email']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = PerevalAddedSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response({'status': status.HTTP_201_CREATED, 'message': 'Запись успешно создана', 'id': obj.id})
        return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': serializer.errors})


class SubmitDetailData(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       generics.GenericAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PerevalAddedDetailSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            if instance.status != 'new':
                raise ValidationError(f'Статус данных изменился на: {instance.status}. Редактирование запрещено')
            serializer.save()
            return Response({'state': 1, 'message': 'Данные успешно отредактированы'})
        return Response({'state': 0, 'message': serializer.errors})