from django.urls import path
from .views import SubmitData, SubmitDetailData

urlpatterns = [
    path('submitData/', SubmitData.as_view(), name='submitData'),
    path('submitData/<int:pk>/', SubmitDetailData.as_view(), name='SubmitDetailData')
]