# Generated by Django 3.2.2 on 2021-05-28 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecursosWebApp', '0018_alter_post_categorias'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='from_signal',
            field=models.BooleanField(default=False),
        ),
    ]
