# Generated by Django 4.2.5 on 2023-10-03 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('survey', '0002_remove_question_title_checksurvey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checksurvey',
            name='survey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.survey', verbose_name='опрос'),
        ),
        migrations.AlterField(
            model_name='checksurvey',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]