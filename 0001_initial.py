# Generated by Django 5.1.2 on 2024-11-06 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('cid', models.IntegerField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=6)),
                ('phno', models.IntegerField(max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('uname', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
