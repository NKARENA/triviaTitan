# Generated by Django 3.2.9 on 2023-12-11 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0003_auto_20231211_1932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='option_1_6',
            new_name='option_1_q6',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='option_2_6',
            new_name='option_2_q6',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='option_3_6',
            new_name='option_3_q6',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='option_4_6',
            new_name='option_4_q6',
        ),
    ]
