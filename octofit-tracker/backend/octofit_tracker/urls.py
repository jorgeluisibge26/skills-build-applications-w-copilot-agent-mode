"""octofit_tracker URL Configuration"""
import os

from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from rest_framework import routers

from .views import (
    ActivityViewSet,
    LeaderboardViewSet,
    TeamViewSet,
    UserViewSet,
    WorkoutViewSet,
)


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)


def api_root(request):
    return JsonResponse({
        'message': 'Welcome to the Octofit Tracker API',
        'status': 'ok',
        'routes': {
            'users': '/api/users/',
            'teams': '/api/teams/',
            'activities': '/api/activities/',
            'leaderboard': '/api/leaderboard/',
            'workouts': '/api/workouts/',
        },
    })


codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root-api'),
    path('api/', include(router.urls)),
]
