# Generated by Django 4.1.2 on 2022-10-12 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0008_remove_ingredient_description_recipe_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.CharField(max_length=250, null=True),
        ),
    ]