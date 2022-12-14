# Generated by Django 4.1.2 on 2022-10-12 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0009_alter_recipe_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(help_text='Enter SI Unit only like kg or ltr or piece', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='quantity',
            field=models.IntegerField(help_text='Enter SI Unit only like kg or ltr or piece'),
        ),
    ]
