from django.core.management.base import BaseCommand

from octofit_tracker.models import Activity, LeaderboardEntry, Team, User, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        Workout.objects.all().delete()

        marvel = Team.objects.create(
            name='Marvel Squad',
            captain='Spider-Man',
            description='Equipe de super-heróis com foco em velocidade e resistência.',
            points=1250,
        )
        dc = Team.objects.create(
            name='DC Squad',
            captain='Batman',
            description='Equipe de super-heróis com foco em força e estratégia.',
            points=1185,
        )

        users = [
            User(username='spiderman', email='spiderman@octofit.com', first_name='Peter', last_name='Parker', age=22, city='Queens', team='Marvel Squad'),
            User(username='batman', email='batman@octofit.com', first_name='Bruce', last_name='Wayne', age=34, city='Gotham', team='DC Squad'),
            User(username='wonderwoman', email='wonderwoman@octofit.com', first_name='Diana', last_name='Prince', age=30, city='Themyscira', team='DC Squad'),
            User(username='captainamerica', email='captainamerica@octofit.com', first_name='Steve', last_name='Rogers', age=36, city='Brooklyn', team='Marvel Squad'),
            User(username='blackwidow', email='blackwidow@octofit.com', first_name='Natasha', last_name='Romanoff', age=29, city='Moscow', team='Marvel Squad'),
        ]
        User.objects.bulk_create(users)

        activities = [
            Activity(user='spiderman', activity_type='Running', duration_minutes=35, calories_burned=320, date='2026-09-10'),
            Activity(user='batman', activity_type='Strength Training', duration_minutes=50, calories_burned=410, date='2026-09-11'),
            Activity(user='wonderwoman', activity_type='Cycling', duration_minutes=40, calories_burned=380, date='2026-09-12'),
            Activity(user='captainamerica', activity_type='HIIT', duration_minutes=30, calories_burned=340, date='2026-09-13'),
            Activity(user='blackwidow', activity_type='Yoga', duration_minutes=25, calories_burned=210, date='2026-09-14'),
        ]
        Activity.objects.bulk_create(activities)

        leaderboard = [
            LeaderboardEntry(username='spiderman', team='Marvel Squad', score=980, rank=1),
            LeaderboardEntry(username='wonderwoman', team='DC Squad', score=940, rank=2),
            LeaderboardEntry(username='captainamerica', team='Marvel Squad', score=910, rank=3),
            LeaderboardEntry(username='batman', team='DC Squad', score=890, rank=4),
            LeaderboardEntry(username='blackwidow', team='Marvel Squad', score=860, rank=5),
        ]
        LeaderboardEntry.objects.bulk_create(leaderboard)

        workouts = [
            Workout(name='Hero Sprint', focus_area='Cardio', duration_minutes=25, difficulty='Intermediate', trainer='Coach Stark'),
            Workout(name='Power Circuit', focus_area='Strength', duration_minutes=40, difficulty='Advanced', trainer='Coach Wayne'),
            Workout(name='Agility Flow', focus_area='Mobility', duration_minutes=20, difficulty='Beginner', trainer='Coach Diana'),
            Workout(name='Endurance Blast', focus_area='Stamina', duration_minutes=35, difficulty='Intermediate', trainer='Coach Rogers'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(
            self.style.SUCCESS('Populate the octofit_db database with test data complete.')
        )
