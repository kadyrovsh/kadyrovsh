# Generated by Django 4.0.4 on 2022-05-12 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fan',
            name='ustozlar',
            field=models.ManyToManyField(blank=True, to='courses.ustoz'),
        ),
        migrations.AlterField(
            model_name='fan',
            name='yonalish',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='courses.yonalish'),
        ),
        migrations.AlterField(
            model_name='ustoz',
            name='ism',
            field=models.CharField(default=True, max_length=15),
        ),
    ]
