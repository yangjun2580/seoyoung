# Generated by Django 4.0.5 on 2022-06-24 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_newuser_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('profile_image', models.TextField()),
                ('nickname', models.CharField(max_length=24, unique=True)),
                ('name', models.CharField(max_length=24)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(default=False, max_length=255)),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.DeleteModel(
            name='Newuser',
        ),
    ]
