# Generated by Django 4.1.1 on 2022-10-03 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Ejercicio_12_1_Directores_Cine', '0004_remove_movie_director_of_movie_alter_director_movies_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='movies',
            field=models.ManyToManyField(to='App_Ejercicio_12_1_Directores_Cine.movie'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre_of_movie',
            field=models.ManyToManyField(to='App_Ejercicio_12_1_Directores_Cine.genre'),
        ),
    ]