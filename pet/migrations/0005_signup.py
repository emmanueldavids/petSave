# Generated by Django 5.1 on 2024-09-20 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0004_remove_donation_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=300)),
            ],
        ),
    ]
