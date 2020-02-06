# Generated by Django 2.1.5 on 2020-02-04 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('post_pic', models.ImageField(default='recipe_pics/default.jpg', upload_to='recipe_pics')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('ingredients', django_mysql.models.ListCharField(models.CharField(max_length=20), max_length=420, size=20)),
                ('steps', django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=2020, size=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
