from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    city = models.CharField(max_length=100, blank=True, default='')
    team = models.CharField(max_length=100, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'octofit_tracker'

    def __str__(self):
        return self.username


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    captain = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'octofit_tracker'

    def __str__(self):
        return self.name


class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.IntegerField(default=0)
    calories_burned = models.IntegerField(default=0)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'octofit_tracker'

    def __str__(self):
        return f"{self.user} - {self.activity_type}"


class LeaderboardEntry(models.Model):
    username = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    rank = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'octofit_tracker'

    def __str__(self):
        return f"{self.username} ({self.score})"


class Workout(models.Model):
    name = models.CharField(max_length=100)
    focus_area = models.CharField(max_length=100)
    duration_minutes = models.IntegerField(default=0)
    difficulty = models.CharField(max_length=50, default='Beginner')
    trainer = models.CharField(max_length=100, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'octofit_tracker'

    def __str__(self):
        return self.name
