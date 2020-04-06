# Generated by Django 2.2.7 on 2019-12-04 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191204_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('com_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(max_length=20)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blogs')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.users')),
            ],
        ),
    ]
