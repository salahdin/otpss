# Generated by Django 2.2.8 on 2020-06-26 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_userfavoriteassessment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavoriteassessment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myList', to=settings.AUTH_USER_MODEL),
        ),
    ]