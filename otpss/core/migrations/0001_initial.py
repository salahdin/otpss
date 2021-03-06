# Generated by Django 2.2.8 on 2020-02-27 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseCode', models.CharField(max_length=10, verbose_name='assessment course code')),
                ('courseTitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='course title of assessment')),
                ('assessmentDate', models.DateField(blank=True, null=True, verbose_name='day of assessment')),
                ('uploadDate', models.DateTimeField(verbose_name='date and time of upload')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=500, null=True, verbose_name='content of the question')),
                ('date', models.DateTimeField()),
                ('assessment', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='assessment', to='core.Assessment')),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('assessment', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Assessment')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Answercontent', models.CharField(max_length=500, verbose_name='content of question')),
                ('question', models.ManyToManyField(related_name='question', to='core.Question')),
            ],
        ),
    ]
