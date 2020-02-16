from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from taskapp.models import Taskapp, Tagapp


class TaskappTests(APITestCase):

    def setUp(self):
        Taskapp.objects.create(title='Run marathon', description='Need to run a marathon')
        Taskapp.objects.create(title='Lie on the beach', description='Need some more sunlight')

    def test_create_task(self):
        url = reverse('task_list_url')
        data = {'title': 'Buy milk', 'description': 'Need some milk'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Taskapp.objects.get(id=3).title, 'Buy milk')

    def test_get_single_task(self):
        url = reverse('task_detail_url', args=[1])
        # response = self.client.post(url, data, format='json')

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_tasks_list(self):
        url = reverse('task_list_url')
        response = self.client.get(url, format='json')

        # response = self.client.get('127.0.0.1:8000/api/v1/tasks/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TagappTests(APITestCase):

    def setUp(self):
        Taskapp.objects.create(title='bla', description='blabla')
        Tagapp.objects.create(title='marathon')

    def test_create_tag(self):
        url = reverse('tag_list_url')
        data = {'title': 'milk', 'tasks': [1]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tagapp.objects.get(id=2).title, 'milk')

    def test_get_single_tag(self):
        url = reverse('tag_detail_url', args=[1])
        response = self.client.get(url, format='json')

        # response = self.client.get('127.0.0.1:8000/api/v1/tags/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_tags_list(self):
        url = reverse('tag_list_url')
        response = self.client.get(url, format='json')

        # response = self.client.get('127.0.0.1:8000/api/v1/tags/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)