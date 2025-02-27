# Generated by Django 5.0.6 on 2024-05-31 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moto',
            fields=[
                ('idMoto', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('cilindrada', models.IntegerField(max_length=50)),
                ('tipo_moto', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'olivera_moto',
            },
        ),
        migrations.DeleteModel(
            name='Casa',
        ),
    ]
