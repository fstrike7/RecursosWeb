# Generated by Django 3.2.2 on 2021-05-27 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecursosWebApp', '0017_alter_comentario_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categorias',
            field=models.ManyToManyField(to='RecursosWebApp.Categoria', verbose_name='Categoria'),
        ),
    ]
