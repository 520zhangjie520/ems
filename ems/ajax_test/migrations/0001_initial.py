# Generated by Django 2.0.6 on 2019-09-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ajax_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.IntegerField()),
            ],
            options={
                'db_table': 'Ajax_user',
            },
        ),
    ]
