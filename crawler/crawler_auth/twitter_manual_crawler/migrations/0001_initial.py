# Generated by Django 2.2.7 on 2020-04-27 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity_Logger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.TextField(blank=True, null=True)),
                ('activity_app', models.TextField(blank=True, null=True)),
                ('activity_details', models.TextField(blank=True, null=True)),
                ('activity_status', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('username', models.TextField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('join_date', models.TextField(blank=True, null=True)),
                ('join_time', models.TextField(blank=True, null=True)),
                ('tweets', models.TextField(blank=True, null=True)),
                ('following', models.TextField(blank=True, null=True)),
                ('followers', models.TextField(blank=True, null=True)),
                ('likes', models.TextField(blank=True, null=True)),
                ('media', models.TextField(blank=True, null=True)),
                ('is_private', models.TextField(blank=True, null=True)),
                ('is_verified', models.TextField(blank=True, null=True)),
                ('profile_image_url', models.TextField(blank=True, null=True)),
                ('background_image', models.TextField(blank=True, null=True)),
                ('lat', models.TextField(blank=True, null=True)),
                ('lon', models.TextField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('follower_id_fk', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Followings',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('username', models.TextField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('join_date', models.TextField(blank=True, null=True)),
                ('join_time', models.TextField(blank=True, null=True)),
                ('tweets', models.TextField(blank=True, null=True)),
                ('following', models.TextField(blank=True, null=True)),
                ('followers', models.TextField(blank=True, null=True)),
                ('likes', models.TextField(blank=True, null=True)),
                ('media', models.TextField(blank=True, null=True)),
                ('is_private', models.TextField(blank=True, null=True)),
                ('is_verified', models.TextField(blank=True, null=True)),
                ('profile_image_url', models.TextField(blank=True, null=True)),
                ('background_image', models.TextField(blank=True, null=True)),
                ('lat', models.TextField(blank=True, null=True)),
                ('lon', models.TextField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('following_id_fk', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='profiles_target_model',
            fields=[
                ('target_platform', models.CharField(default='twitter', max_length=255)),
                ('target_type', models.CharField(default='profile_target', max_length=255)),
                ('twitter_username', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('target_scheduling', models.CharField(choices=[('', 'Select Target Scheuling'), ('1hr', 'Every One Hour'), ('6hr', 'Every Six Hour'), ('12hr', 'Every Twelve Hour'), ('24hr', 'Every Day ')], max_length=255)),
                ('scanning_status', models.CharField(default='pending', max_length=255)),
                ('followers_count', models.CharField(default='0', max_length=255)),
                ('followings_count', models.CharField(default='0', max_length=255)),
                ('tweets_count', models.CharField(default='0', max_length=255)),
                ('profile_img_url', models.CharField(default='0', max_length=255)),
                ('background_image', models.CharField(default='0', max_length=255)),
                ('username', models.CharField(default='0', max_length=255)),
                ('name', models.CharField(default='0', max_length=255)),
                ('media', models.CharField(default='0', max_length=255)),
                ('location', models.CharField(default='0', max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('followers_fkey', models.CharField(default='0', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('id_str', models.TextField(blank=True, null=True)),
                ('conversation_id', models.TextField(blank=True, null=True)),
                ('datetime', models.TextField(blank=True, null=True)),
                ('datestamp', models.TextField(blank=True, null=True)),
                ('timestamp', models.TextField(blank=True, null=True)),
                ('user_id', models.TextField(blank=True, null=True)),
                ('user_id_str', models.TextField(blank=True, null=True)),
                ('username', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('place', models.TextField(blank=True, null=True)),
                ('timezone', models.TextField(blank=True, null=True)),
                ('mentions', models.TextField(blank=True, null=True)),
                ('urls', models.TextField(blank=True, null=True)),
                ('photos', models.TextField(blank=True, null=True)),
                ('video', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('hashtags', models.TextField(blank=True, null=True)),
                ('cashtags', models.TextField(blank=True, null=True)),
                ('replies_count', models.TextField(blank=True, null=True)),
                ('likes_count', models.TextField(blank=True, null=True)),
                ('retweets_count', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('user_rt_id', models.TextField(blank=True, null=True)),
                ('retweet', models.TextField(blank=True, null=True)),
                ('retweet_id', models.TextField(blank=True, null=True)),
                ('retweet_date', models.TextField(blank=True, null=True)),
                ('quote_url', models.TextField(blank=True, null=True)),
                ('near', models.TextField(blank=True, null=True)),
                ('geo', models.TextField(blank=True, null=True)),
                ('source', models.TextField(blank=True, null=True)),
                ('reply_to', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tweets_target_model',
            fields=[
                ('target_platform', models.CharField(default='twitter', max_length=255)),
                ('target_type', models.CharField(default='tweets_target', max_length=255)),
                ('twitter_username', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('target_scheduling', models.CharField(choices=[('', 'Select Target Scheuling'), ('1hr', 'Every One Hour'), ('6hr', 'Every Six Hour'), ('12hr', 'Every Twelve Hour'), ('24hr', 'Every Day ')], max_length=255)),
                ('scanning_status', models.CharField(default='pending', max_length=255)),
                ('tweets_count', models.CharField(default='0', max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('id_str', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('username', models.TextField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('join_date', models.TextField(blank=True, null=True)),
                ('join_time', models.TextField(blank=True, null=True)),
                ('tweets', models.TextField(blank=True, null=True)),
                ('following', models.TextField(blank=True, null=True)),
                ('followers', models.TextField(blank=True, null=True)),
                ('likes', models.TextField(blank=True, null=True)),
                ('media', models.TextField(blank=True, null=True)),
                ('private', models.TextField(blank=True, null=True)),
                ('verified', models.TextField(blank=True, null=True)),
                ('profile_image_url', models.TextField(blank=True, null=True)),
                ('background_image', models.TextField(blank=True, null=True)),
                ('lat', models.TextField(blank=True, null=True)),
                ('lon', models.TextField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
