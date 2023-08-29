from django.test import TestCase
from .models import PerevalAdded
from .serializers import PerevalAddedSerializer


class PerevalAddedModelTest(TestCase):

    def setUp(self):
        self.pereval = PerevalAdded.objects.create(beautyTitle="Тестовый заголовок", status="new")

    def test_pereval_created(self):
        self.assertEqual(self.pereval.beautyTitle, "Тестовый заголовок")
        self.assertEqual(self.pereval.status, "new")


class SubmitDataAPITest(TestCase):

    def test_submit_data(self):
        data = {
            "beautyTitle": "Новый объект",
            "status": "new"
        }
        response = self.client.post('/api/submitData/', data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(PerevalAdded.objects.count(), 1)