# Generated by Django 3.1.3 on 2020-11-29 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph_no', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
