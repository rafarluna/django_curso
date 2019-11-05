# Generated by Django 2.2.6 on 2019-10-26 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha_pedido',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='total',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
    ]
