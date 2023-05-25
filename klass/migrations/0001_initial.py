# Generated by Django 4.2.1 on 2023-05-25 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название урока')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, verbose_name='имя')),
                ('lastname', models.CharField(max_length=100, verbose_name='фамилия')),
                ('email', models.EmailField(help_text='Введите ваш email', max_length=100, verbose_name='email')),
                ('phone', models.CharField(max_length=100, verbose_name='телефон')),
                ('adress', models.CharField(max_length=100, verbose_name='адресс')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистраций')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='klass.subject', verbose_name='урок')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, verbose_name='имя')),
                ('lastname', models.CharField(max_length=100, verbose_name='фамилия')),
                ('email', models.EmailField(help_text='Введите ваш email', max_length=100, verbose_name='email')),
                ('phone', models.CharField(max_length=100, verbose_name='телефон')),
                ('adress', models.CharField(max_length=100, verbose_name='адресс')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='klass.teacher', verbose_name='Преподаватель')),
            ],
            options={
                'verbose_name': 'Ученик(ца)',
                'verbose_name_plural': 'Ученики(цы)',
            },
        ),
        migrations.CreateModel(
            name='Klass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(verbose_name='Номер класса')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='klass.teacher', verbose_name='преподаватель')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
            },
        ),
    ]