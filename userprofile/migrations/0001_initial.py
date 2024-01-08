# Generated by Django 4.2.6 on 2023-10-06 06:51

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
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='cover_images/')),
                ('about', models.TextField(blank=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('relationship_status', models.CharField(blank=True, choices=[('Single', 'Single'), ('In a relationship', 'In a relationship'), ('Engaged', 'Engaged'), ('Married', 'Married'), ('Complicated', 'Complicated')], max_length=20)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=3)),
                ('email_address', models.EmailField(blank=True, max_length=254)),
                ('website', models.URLField(blank=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('hobbies', models.TextField(blank=True)),
                ('favourite_movies', models.TextField(blank=True)),
                ('favourite_books', models.TextField(blank=True)),
                ('favourite_games', models.TextField(blank=True)),
                ('favourite_bands_artists', models.TextField(blank=True)),
                ('favourite_series', models.TextField(blank=True)),
                ('other_interest', models.TextField(blank=True)),
                ('education', models.TextField(blank=True)),
                ('work', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]