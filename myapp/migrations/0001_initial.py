# Generated by Django 3.0.2 on 2020-10-12 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=30)),
                ('cname', models.CharField(max_length=100)),
                ('camount', models.FloatField()),
                ('cproduct', models.CharField(max_length=30)),
                ('sdate', models.CharField(max_length=30)),
                ('edate', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=30)),
                ('prname', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('suname', models.CharField(max_length=30)),
                ('scname', models.CharField(max_length=30)),
                ('dis', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vname', models.CharField(max_length=30)),
                ('vproduct', models.CharField(max_length=30)),
                ('quality', models.CharField(max_length=100)),
                ('rdeli', models.CharField(max_length=30)),
                ('rprice', models.FloatField()),
                ('service', models.CharField(max_length=30)),
                ('risk', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=30)),
                ('ename', models.CharField(max_length=100)),
                ('sname', models.CharField(max_length=30)),
                ('pname', models.CharField(max_length=30)),
                ('sprice', models.FloatField()),
                ('eemail', models.EmailField(max_length=254)),
                ('econtact', models.CharField(max_length=30)),
            ],
        ),
    ]
