# Generated by Django 2.1.5 on 2019-04-09 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_chlenkomissii_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chlenkomissii',
            options={'verbose_name': 'Член комиссии', 'verbose_name_plural': 'Члены комиссии'},
        ),
        migrations.AlterField(
            model_name='chlenkomissii',
            name='udost_type',
            field=models.CharField(choices=[('Персонал', 'Персонал'), ('Материалы', 'Материалы'), ('Оборудование', 'Оборудование'), ('Технологии', 'Технологии'), ('Оценка квалификации', 'Оценка квалификации')], default='Персонал', max_length=20, verbose_name='Тип удостоверения'),
        ),
    ]