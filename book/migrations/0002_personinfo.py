# Generated by Django 2.2.5 on 2021-07-28 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('gender', models.IntegerField(choices=[(1, 'male'), (2, 'female')])),
                ('description', models.CharField(max_length=100, null=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.BookInfo')),
            ],
            options={
                'db_table': 'personinfo',
            },
        ),
    ]
