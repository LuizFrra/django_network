# Generated by Django 5.1.3 on 2024-12-03 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField(max_length=512)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]