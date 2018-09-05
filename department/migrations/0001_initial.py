# Generated by Django 2.0.3 on 2018-09-03 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=300)),
                ('fees', models.CharField(default='0', max_length=100)),
                ('trainer_name', models.CharField(max_length=200)),
            ],
        ),
    ]