# Generated by Django 2.2 on 2020-10-02 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gricapi', '0005_auto_20201002_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(db_index=True, default='General', max_length=200),
        ),
    ]