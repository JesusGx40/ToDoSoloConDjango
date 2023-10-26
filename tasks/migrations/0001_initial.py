# Generated by Django 4.2.6 on 2023-10-25 21:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('completado', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('due_date', models.DateField()),
                ('due_time', models.TimeField()),
            ],
        ),
    ]