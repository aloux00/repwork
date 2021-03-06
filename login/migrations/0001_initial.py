# Generated by Django 2.0 on 2018-01-11 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hosname', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examnum', models.CharField(max_length=32, null=True)),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=32)),
                ('age', models.CharField(max_length=32)),
                ('ageunit', models.CharField(max_length=32)),
                ('examtype', models.CharField(max_length=32)),
                ('position', models.CharField(max_length=80)),
                ('method', models.CharField(max_length=80)),
                ('hospital', models.CharField(max_length=80)),
                ('indication', models.CharField(blank=True, max_length=150, null=True)),
                ('findings', models.TextField()),
                ('comments', models.TextField(blank=True, null=True)),
                ('examdate', models.CharField(max_length=50)),
                ('reportdate', models.CharField(max_length=50)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('repdoctor', models.CharField(max_length=50)),
                ('status', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='reptemplates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repname', models.CharField(max_length=50)),
                ('findings', models.CharField(max_length=1200)),
                ('comments', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=128)),
                ('levels', models.CharField(max_length=32)),
                ('permission', models.IntegerField()),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ['-c_time'],
            },
        ),
        migrations.AddField(
            model_name='reptemplates',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='login.user'),
        ),
    ]
