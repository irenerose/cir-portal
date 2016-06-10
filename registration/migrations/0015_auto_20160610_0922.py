# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0014_auto_20160610_0513'),
    ]

    operations = [
        migrations.CreateModel(
            name='AptitudeTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(verbose_name='Mark', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EligibilityTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(verbose_name='Mark', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='HRTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(verbose_name='Mark', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuantitativeTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(verbose_name='Mark', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReasoningTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(verbose_name='Mark', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TechTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(verbose_name='Mark', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='VerbalsTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(verbose_name='Mark', blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='curr_arrears',
            field=models.IntegerField(null=True, verbose_name='No of current arrears', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='hist_arrears',
            field=models.IntegerField(null=True, verbose_name='No of history arrears', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='tenth_mark',
            field=models.CharField(max_length=5, null=True, verbose_name='10th Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='twelth_mark',
            field=models.CharField(max_length=5, null=True, verbose_name='12th Mark', blank=True),
        ),
        migrations.AddField(
            model_name='verbalstest',
            name='student',
            field=models.ForeignKey(to='registration.Student'),
        ),
        migrations.AddField(
            model_name='verbalstest',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
        migrations.AddField(
            model_name='techtest',
            name='student',
            field=models.ForeignKey(to='registration.Student'),
        ),
        migrations.AddField(
            model_name='techtest',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
        migrations.AddField(
            model_name='reasoningtest',
            name='student',
            field=models.ForeignKey(to='registration.Student'),
        ),
        migrations.AddField(
            model_name='reasoningtest',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
        migrations.AddField(
            model_name='quantitativetest',
            name='student',
            field=models.ForeignKey(to='registration.Student'),
        ),
        migrations.AddField(
            model_name='quantitativetest',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
        migrations.AddField(
            model_name='hrtest',
            name='student',
            field=models.ForeignKey(to='registration.Student'),
        ),
        migrations.AddField(
            model_name='hrtest',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
        migrations.AddField(
            model_name='eligibilitytest',
            name='student',
            field=models.ForeignKey(to='registration.Student'),
        ),
        migrations.AddField(
            model_name='eligibilitytest',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
        migrations.AddField(
            model_name='aptitudetest',
            name='student',
            field=models.ForeignKey(to='registration.Student'),
        ),
        migrations.AddField(
            model_name='aptitudetest',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
    ]
