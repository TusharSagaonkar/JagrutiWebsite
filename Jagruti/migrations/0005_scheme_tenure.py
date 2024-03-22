# Generated by Django 5.0.2 on 2024-03-18 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jagruti', '0004_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tenure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenure', models.CharField(max_length=100)),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('scheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tenures', to='Jagruti.scheme')),
            ],
            options={
                'unique_together': {('scheme', 'tenure')},
            },
        ),
    ]