# Generated by Django 4.0 on 2022-03-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_product_prod_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_img',
            field=models.ImageField(blank=True, default='prodImage/default_img.png', upload_to='prodImage/'),
        ),
    ]
