# Generated by Django 2.2.6 on 2019-10-25 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagebyuser',
            name='operation',
            field=models.CharField(choices=[('erosion', 'Erosion'), ('dilation', 'Dilation'), ('opening', 'Opening'), ('closing', 'Closing'), ('morphological Gradient', 'Morphological Gradient'), ('tophat', 'Tophat'), ('blackhat', 'Blackhat')], default='erosion', max_length=50),
        ),
        migrations.AddField(
            model_name='imagebyuser',
            name='structural_element',
            field=models.IntegerField(choices=[(0, 'Rectangle'), (2, 'Ellipse'), (1, 'Cross')], default=0),
        ),
        migrations.AddField(
            model_name='imagebyuser',
            name='structural_element_size',
            field=models.IntegerField(default=5),
        ),
    ]
