# Generated by Django 2.2.8 on 2020-03-31 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200330_0038'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssessmentFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='answer',
            name='Answercontent',
            field=models.TextField(verbose_name='content of question'),
        ),
    ]
