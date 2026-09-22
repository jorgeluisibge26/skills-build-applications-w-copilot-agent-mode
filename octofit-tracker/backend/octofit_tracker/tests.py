from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Activity, Team, User, Workout


class OctofitTrackerTests(TestCase):
    def test_api_root_and_root_route(self):
        root_response = self.client.get('/')
        self.assertEqual(root_response.status_code, 200)
        self.assertIn('message', root_response.json())

        api_response = self.client.get(reverse('api-root'))
        self.assertEqual(api_response.status_code, 200)
        self.assertIn('routes', api_response.json())

    def test_user_creation_and_listing(self):
        user = User.objects.create(
            username='spiderman',
            email='spiderman@octofit.com',
            first_name='Peter',
            last_name='Parker',
            age=22,
            city='Queens',
            team='Marvel Squad',
        )
        self.assertEqual(User.objects.count(), 1)

        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        items = payload if isinstance(payload, list) else payload.get('results', [])
        self.assertGreaterEqual(len(items), 1)
        self.assertEqual(User.objects.count(), 1)

    def test_team_creation_and_listing(self):
        Team.objects.create(
            name='Marvel Squad',
            captain='Spider-Man',
            description='Speed and endurance',
            points=1250,
        )

        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Team.objects.count(), 1)

    def test_activity_creation_and_listing(self):
        Activity.objects.create(
            user='spiderman',
            activity_type='Running',
            duration_minutes=35,
            calories_burned=320,
            date=date(2026, 9, 10),
        )

        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Activity.objects.count(), 1)

    def test_workout_creation_and_listing(self):
        Workout.objects.create(
            name='Hero Sprint',
            focus_area='Cardio',
            duration_minutes=25,
            difficulty='Intermediate',
            trainer='Coach Stark',
        )

        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Workout.objects.count(), 1)
