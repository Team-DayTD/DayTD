# Generated by Django 4.0 on 2022-08-06 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_ouruser_delete_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ouruser',
            old_name='birthday',
            new_name='birth',
        ),
        migrations.AlterField(
            model_name='ouruser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='ouruser',
            name='gender',
            field=models.CharField(choices=[('W', 'woman'), ('M', 'man'), ('No', 'none')], max_length=2),
        ),
    ]
