# Generated by Django 3.1.5 on 2021-01-20 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('air_img', models.FileField(upload_to='air_imag/')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_place', models.CharField(max_length=50)),
                ('arrival_place', models.CharField(max_length=50)),
                ('departure_airport', models.CharField(max_length=10)),
                ('arrival_airport', models.CharField(max_length=10)),
                ('departure_time', models.TimeField()),
                ('arrival_time', models.TimeField()),
                ('departure_data', models.DateField()),
                ('first_class_price', models.IntegerField()),
                ('business_class_price', models.IntegerField()),
                ('premium_price', models.IntegerField()),
                ('economy_price', models.IntegerField()),
                ('airline_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='air_app.airline')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date', models.DateField(auto_now_add=True)),
                ('price', models.IntegerField()),
                ('come_ticket_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='come_ticket', to='air_app.ticket')),
                ('go_ticket_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='go_ticket', to='air_app.ticket')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='user_app.user')),
            ],
        ),
    ]
