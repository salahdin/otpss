# Generated by Django 2.2.8 on 2020-03-19 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200313_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservotes',
            name='vote_type',
            field=models.CharField(choices=[('U', 'upvote'), ('D', 'downvote')], max_length=10),
        ),
    ]
