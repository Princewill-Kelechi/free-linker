# Generated by Django 3.2.7 on 2021-09-16 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('freelinks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkproject',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='linkproject',
            name='project_name',
            field=models.CharField(blank=True, db_index=True, max_length=20, null=True, unique=True),
        ),
    ]