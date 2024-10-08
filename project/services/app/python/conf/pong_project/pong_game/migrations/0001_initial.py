# Generated by Django 4.2.14 on 2024-09-14 11:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('max_participants', models.IntegerField()),
                ('status', models.CharField(choices=[('REGISTRATION', 'Registration Open'), ('IN_PROGRESS', 'In Progress'), ('FINISHED', 'Finished')], default='REGISTRATION', max_length=20)),
                ('current_round', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_tournaments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TournamentParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=50)),
                ('eliminated', models.BooleanField(default=False)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='pong_game.tournament')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('tournament', 'alias')},
            },
        ),
        migrations.CreateModel(
            name='TournamentMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.IntegerField()),
                ('score_player1', models.IntegerField(default=0)),
                ('score_player2', models.IntegerField(default=0)),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_player1', to='pong_game.tournamentparticipant')),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_player2', to='pong_game.tournamentparticipant')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='pong_game.tournament')),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches_won', to='pong_game.tournamentparticipant')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournaments_won', models.IntegerField(default=0)),
                ('tournaments_participated', models.IntegerField(default=0)),
                ('highest_score', models.IntegerField(default=0)),
                ('total_time_played', models.DurationField(default=datetime.timedelta(0))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stats', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MatchRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('max_players', models.IntegerField(default=2)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_lobbies', to=settings.AUTH_USER_MODEL)),
                ('players', models.ManyToManyField(related_name='joined_lobbies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_player1', models.IntegerField(default=0)),
                ('score_player2', models.IntegerField(default=0)),
                ('date_played', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('WAITING', 'Waiting'), ('IN_PROGRESS', 'In Progress'), ('FINISHED', 'Finished')], default='WAITING', max_length=20)),
                ('round', models.IntegerField(default=1)),
                ('is_tournament_game', models.BooleanField(default=False)),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_as_player1', to=settings.AUTH_USER_MODEL)),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_as_player2', to=settings.AUTH_USER_MODEL)),
                ('tournament', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pong_game.tournament')),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='games_won', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
