# Generated by Django 4.0.5 on 2022-06-24 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.TextField()),
                ('nickname', models.CharField(max_length=45, unique=True)),
                ('name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45, unique=True)),
                ('password', models.CharField(max_length=45)),
                ('required_fields', models.CharField(blank=True, db_column='REQUIRED_FIELDS', max_length=45, null=True)),
                ('username_field', models.CharField(blank=True, db_column='USERNAME_FIELD', max_length=45, null=True)),
            ],
            options={
                'db_table': 'newuser',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
