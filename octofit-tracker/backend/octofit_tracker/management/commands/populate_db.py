from django.core.management.base import BaseCommand
from tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor', password='password1'),
            User(email='metalgeek@mhigh.edu', name='Tony Stark', password='password2'),
            User(email='zerocool@mhigh.edu', name='Steve Rogers', password='password3'),
            User(email='crashoverride@hmhigh.edu', name='Natasha Romanoff', password='password4'),
            User(email='sleeptoken@mhigh.edu', name='Bruce Banner', password='password5'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(name='Blue Team')
        team2 = Team(name='Gold Team')
        team1.save()
        team2.save()

        # Create activities
        activities = [
            Activity(user=users[0], activity_type='Cycling', duration=60),
            Activity(user=users[1], activity_type='Crossfit', duration=120),
            Activity(user=users[2], activity_type='Running', duration=90),
            Activity(user=users[3], activity_type='Strength', duration=30),
            Activity(user=users[4], activity_type='Swimming', duration=75),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=team1, score=100),
            Leaderboard(team=team2, score=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
