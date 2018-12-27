# Generated by Django 2.1.4 on 2018-12-27 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pubtime', models.DateField(verbose_name='日期')),
                ('mood', models.FloatField(verbose_name='心情')),
                ('consume', models.TextField(default='', verbose_name='消费')),
                ('time', models.TextField(default='', verbose_name='时间')),
                ('log', models.TextField(default='', verbose_name='记录')),
            ],
            options={
                'verbose_name_plural': '数据',
            },
        ),
    ]
