# Generated by Django 5.0.2 on 2024-03-10 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_rename_gmail_signupdetails_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='postdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length='10000')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
