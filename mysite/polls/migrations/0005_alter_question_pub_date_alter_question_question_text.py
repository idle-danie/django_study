# Generated by Django 4.2.1 on 2023-05-27 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='생성일'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, verbose_name='질문'),
        ),
    ]
