# Generated by Django 5.2 on 2025-04-26 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageConversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conversation_replied', models.BooleanField(default=False)),
                ('reply_message', models.TextField(blank=True, null=True)),
                ('conversation', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='PageSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pageid', models.TextField(blank=True, null=True)),
                ('access_token', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ver_code', models.TextField(blank=True, null=True)),
                ('mobile_ver_flg', models.BooleanField(default=False)),
                ('email_ver_flg', models.BooleanField(default=False)),
                ('pre_charity_org', models.IntegerField(default=0)),
                ('ad_view_total', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.TextField(blank=True, null=True)),
                ('last_upd', models.DateTimeField(auto_now_add=True)),
                ('last_upd_by', models.TextField(blank=True, null=True)),
                ('likes_pulled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.JSONField()),
            ],
        ),
    ]
