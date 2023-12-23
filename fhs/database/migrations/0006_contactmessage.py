# Generated by Django 4.1.7 on 2023-05-06 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
