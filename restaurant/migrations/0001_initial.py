# Generated by Django 5.0.2 on 2024-02-09 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('No_of_guests', models.IntegerField()),
                ('BookingDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Inventory', models.IntegerField()),
            ],
        ),
    ]