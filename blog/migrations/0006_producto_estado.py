# Generated by Django 2.1.2 on 2018-12-12 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_producto_idlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='estado',
            field=models.CharField(default='pendiente', max_length=255),
        ),
    ]