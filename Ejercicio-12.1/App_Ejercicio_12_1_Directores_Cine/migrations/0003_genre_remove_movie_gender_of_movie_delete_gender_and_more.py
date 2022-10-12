# Generated by Django 4.1.1 on 2022-10-03 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Ejercicio_12_1_Directores_Cine', '0002_rename_genre_movie_gender_of_movie_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Genre of the movie', max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='gender_of_movie',
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_of_movie',
            field=models.ManyToManyField(to='App_Ejercicio_12_1_Directores_Cine.genre'),
        ),
    ]
