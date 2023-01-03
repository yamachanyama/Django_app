# Generated by Django 4.0.6 on 2023-01-03 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='コメント内容')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hello3.comment', verbose_name='親コメント')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello3.message', verbose_name='対象記事')),
            ],
        ),
    ]
