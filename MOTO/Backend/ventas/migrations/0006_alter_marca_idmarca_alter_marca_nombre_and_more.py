# Generated by Django 5.0.4 on 2024-06-14 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0005_alter_marca_idmarca_alter_marca_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='idMarca',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='marca',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tipomoto',
            name='idTipoMoto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tipomoto',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
