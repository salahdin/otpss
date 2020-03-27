# Generated by Django 2.2.8 on 2020-03-24 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200320_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='assessment description'),
        ),
        migrations.AlterField(
            model_name='question',
            name='assessment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='assessmentQuestion', to='core.Assessment'),
        ),
    ]
