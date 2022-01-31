# Generated by Django 4.0.1 on 2022-01-28 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('date_published', models.DateField()),
                ('image', models.ImageField(default='-', max_length=255, upload_to='books')),
                ('author_id', models.ManyToManyField(to='app.Author')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'db_table': 'books',
                'ordering': ['id'],
            },
        ),
    ]
