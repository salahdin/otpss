# Generated by Django 2.2.8 on 2020-05-08 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_answer_answerimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessmentfile',
            name='assessment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='assessmentdoc', to='core.Assessment'),
        ),
        migrations.AddField(
            model_name='assessmentfile',
            name='document',
            field=models.FileField(null=True, upload_to='', verbose_name='assessment in document format'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='AnswerImage',
            field=models.ImageField(blank=True, null=True, upload_to='answerImage/', verbose_name='answer image'),
        ),
    ]
