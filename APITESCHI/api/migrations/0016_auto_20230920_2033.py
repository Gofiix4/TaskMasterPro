# Generated by Django 3.2.4 on 2023-09-21 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_usuarios_fecha_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='Contrasena',
            field=models.CharField(db_column='Contrasena', default='contra123', max_length=64),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='Correo',
            field=models.CharField(db_column='Correo', default='algo@algo.algo', max_length=50),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='Telefono',
            field=models.IntegerField(db_column='Telefono', default=0),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='ApellidoM',
            field=models.CharField(db_column='ApellidoM', default='apellidom', max_length=45),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='ApellidoP',
            field=models.CharField(db_column='ApellidoP', default='apellidop', max_length=45),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='Fecha_nacimiento',
            field=models.DateField(db_column='Fecha_nacimiento', default='1900/01/01'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='Nombre',
            field=models.CharField(db_column='Nombre', default='nombre', max_length=45),
        ),
    ]
