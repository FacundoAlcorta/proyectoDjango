# Generated by Django 4.1.7 on 2023-03-17 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lineapedido',
            old_name='pedidos_id',
            new_name='pedidos',
        ),
        migrations.RenameField(
            model_name='lineapedido',
            old_name='producto_id',
            new_name='producto',
        ),
    ]
