# Generated by Django 4.2.5 on 2023-10-04 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('survey', '0003_alter_checksurvey_survey_alter_checksurvey_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False, verbose_name='лайк')),
                ('dislike', models.BooleanField(default=False, verbose_name='дизлайк')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.survey', verbose_name='опрос')),
            ],
            options={
                'verbose_name': 'оценка',
                'verbose_name_plural': 'оценки',
            },
        ),
    ]