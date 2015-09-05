# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('answer_id', models.AutoField(serialize=False, primary_key=True)),
                ('question', models.CharField(max_length=300)),
                ('question_link', models.URLField(unique=True)),
                ('author', models.CharField(max_length=200)),
                ('author_link', models.URLField(blank=True)),
                ('vote', models.PositiveIntegerField()),
                ('summary_img', models.TextField(blank=True)),
                ('summary_text', models.TextField()),
                ('answer', models.TextField()),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'answers',
                'managed': False,
                'verbose_name_plural': 'Answers',
            },
        ),
    ]
