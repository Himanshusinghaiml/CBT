# Generated by Django 4.2.6 on 2023-10-29 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companylogin', '0009_questions_alter_centers_profile_pic'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Centers',
            new_name='Center',
        ),
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
        migrations.RenameModel(
            old_name='Tests',
            new_name='Test',
        ),
    ]