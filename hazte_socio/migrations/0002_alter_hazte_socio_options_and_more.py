# Generated by Django 4.0.4 on 2022-06-07 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hazte_socio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hazte_socio',
            options={'verbose_name': 'Socio', 'verbose_name_plural': 'Socios'},
        ),
        migrations.AddField(
            model_name='hazte_socio',
            name='imagen_documento',
            field=models.ImageField(null=True, upload_to='socios'),
        ),
    ]