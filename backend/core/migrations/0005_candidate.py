# Generated by Django 5.1.4 on 2024-12-26 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_county_volunteer_ward_delete_candidate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=1000000)),
                ('position', models.CharField(default='', max_length=1000)),
                ('about', models.TextField(default='')),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.county')),
                ('ward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ward')),
            ],
        ),
    ]