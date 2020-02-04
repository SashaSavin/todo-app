# Generated by Django 3.0.3 on 2020-02-04 08:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('a01a4dd7-fe3f-4528-b73a-3d65b9735f3d'), editable=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('a01a4dd7-fe3f-4528-b73a-3d65b9735f3d'), editable=False),
        ),
    ]