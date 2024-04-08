# Generated by Django 4.2.5 on 2024-03-21 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_contact_first_name_alter_contact_surname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='description',
            field=models.TextField(default='Description', max_length=2500),
        ),
        migrations.AlterField(
            model_name='staff',
            name='description_en',
            field=models.TextField(default='Description', max_length=2500, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='description_sv',
            field=models.TextField(default='Description', max_length=2500, null=True),
        ),
    ]