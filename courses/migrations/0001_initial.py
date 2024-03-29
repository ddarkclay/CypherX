# Generated by Django 2.2.2 on 2019-07-23 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(default='', max_length=100)),
                ('category', models.CharField(default='', max_length=50)),
                ('subject', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=1000)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='courses/images')),
            ],
        ),
    ]
