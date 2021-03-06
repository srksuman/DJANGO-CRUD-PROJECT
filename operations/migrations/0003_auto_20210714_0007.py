# Generated by Django 3.2.5 on 2021-07-13 18:22

from django.db import migrations, models
import operations.models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0002_alter_student_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='full_name',
            field=models.CharField(error_messages={'required': 'You cannot leave name field empty'}, help_text='Enter your full name', max_length=70),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.IntegerField(help_text='Your number must contain 10 digits', validators=[operations.models.Student.checknumber]),
        ),
    ]
