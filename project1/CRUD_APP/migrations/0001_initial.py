# Generated by Django 4.1.2 on 2022-10-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Custumor',
            fields=[
                ('c_id', models.IntegerField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('bill', models.FloatField()),
            ],
        ),
    ]
