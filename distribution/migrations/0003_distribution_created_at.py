# Generated by Django 4.2.2 on 2023-07-10 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribution', '0002_distribution_delete_student_delete_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='distribution',
            name='created_at',
            field=models.DateTimeField(default=None),
        ),
    ]
