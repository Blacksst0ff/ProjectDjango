# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('libelle', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Etape',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('libelle', models.CharField(max_length=50)),
                ('ordre', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('type', models.CharField(max_length=50)),
                ('libelle', models.CharField(max_length=50)),
                ('quantite', models.IntegerField()),
                ('unite', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('valeur', models.IntegerField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('4', '4'), ('5', '5')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recette',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('type_recette', models.CharField(choices=[('0', 'Apéro'), ('1', 'Entrée'), ('2', 'Plat'), ('4', 'Dessert')], max_length=15)),
                ('titre', models.CharField(max_length=50)),
                ('difficulte', models.CharField(choices=[('0', 'Très facile'), ('1', 'Facile'), ('2', 'Normal'), ('4', 'Difficile'), ('5', 'Over 9000')], max_length=15)),
                ('cout', models.IntegerField()),
                ('photo', models.CharField(max_length=250)),
                ('temps_preparation', models.IntegerField()),
                ('temps_cuisson', models.IntegerField()),
                ('temps_repos', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='note',
            name='id_recette',
            field=models.ForeignKey(to='recettes.Recette'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='id_recette',
            field=models.ForeignKey(to='recettes.Recette'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='etape',
            name='id_recette',
            field=models.ForeignKey(to='recettes.Recette'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commentaire',
            name='id_recette',
            field=models.ForeignKey(to='recettes.Recette'),
            preserve_default=True,
        ),
    ]
