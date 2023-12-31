# Generated by Django 4.2.6 on 2023-10-22 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companylogin', '0008_alter_centers_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=512)),
                ('option_1', models.CharField(max_length=256)),
                ('option_2', models.CharField(max_length=256)),
                ('option_3', models.CharField(max_length=256)),
                ('option_4', models.CharField(max_length=256)),
                ('correct_option', models.CharField(max_length=256)),
                ('marks', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='centers',
            name='profile_pic',
            field=models.FileField(default=None, null=True, upload_to='profile_pic/'),
        ),
    ]
