# Generated by Django 5.1.4 on 2024-12-13 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml_plateform', '0003_alter_heartfailure_chestpaintype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heartfailure',
            name='Age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='heartfailure',
            name='ChestPainType',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='heartfailure',
            name='ExerciseAngina',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='heartfailure',
            name='FastingBS',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='heartfailure',
            name='HeartDisease',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='heartfailure',
            name='MaxHR',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='heartfailure',
            name='ST_Slope',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='heartfailure',
            name='Sex',
            field=models.IntegerField(),
        ),
    ]
