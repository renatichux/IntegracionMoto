# Generated by Django 5.0.4 on 2024-06-14 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_cliente_marca_tipomoto_alter_moto_cilindrada_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cliente',
            table='cliente',
        ),
        migrations.AlterModelTable(
            name='detallepedido',
            table='detallepedido',
        ),
        migrations.AlterModelTable(
            name='marca',
            table='marca',
        ),
        migrations.AlterModelTable(
            name='moto',
            table='moto',
        ),
        migrations.AlterModelTable(
            name='pedido',
            table='pedido',
        ),
        migrations.AlterModelTable(
            name='tipomoto',
            table='tipomoto',
        ),
    ]
