# Generated by Django 3.0.2 on 2020-10-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename_f', models.CharField(max_length=10)),
                ('ename_l', models.CharField(max_length=10)),
                ('econtact', models.CharField(max_length=10)),
                ('egender', models.CharField(max_length=20)),
                ('ehometown', models.CharField(max_length=20)),
            ],
        ),
    ]
