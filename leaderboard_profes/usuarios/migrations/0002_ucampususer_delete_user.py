# Generated by Django 4.2.6 on 2023-10-15 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UcampusUser',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('ucampus_login', models.CharField(max_length=255)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='usuarios.major')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
