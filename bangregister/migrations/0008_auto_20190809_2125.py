# Generated by Django 2.1.7 on 2019-08-09 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bangregister', '0007_auto_20190801_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Scrap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='address1',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='address2',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='address3',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='address4',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='elevator',
            field=models.CharField(choices=[('있음', '있음'), ('없음', '없음')], max_length=128),
        ),
        migrations.AlterField(
            model_name='room',
            name='host_stuff',
            field=models.CharField(choices=[('있음', '있음'), ('없음', '없음')], max_length=128),
        ),
        migrations.AlterField(
            model_name='room',
            name='main_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='room',
            name='option',
            field=models.CharField(choices=[('에어컨', '에어컨'), ('냉장고', '냉장고'), ('세탁기', '세탁기'), ('책상', '책상'), ('침대', '침대'), ('침대', '싱크대')], max_length=128),
        ),
        migrations.AlterField(
            model_name='room',
            name='other_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='room',
            name='parking',
            field=models.CharField(choices=[('있음', '있음'), ('없음', '없음')], max_length=128),
        ),
        migrations.AlterField(
            model_name='room',
            name='pet',
            field=models.CharField(choices=[('가능', '가능'), ('불가능', '불가능')], max_length=128),
        ),
        migrations.AlterField(
            model_name='room',
            name='rent_term',
            field=models.CharField(choices=[('장기(2주이상)', '장기(2주이상)'), ('단기(2주미만)', '단기(2주미만)')], max_length=128),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('원룸', '원룸'), ('투룸', '투룸'), ('복층형 원룸', '복층형 원룸'), ('쓰리룸+', '쓰리룸+')], max_length=128),
        ),
        migrations.AddField(
            model_name='scrap',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangregister.Room'),
        ),
        migrations.AddField(
            model_name='scrap',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='like',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangregister.Room'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='room',
            name='users',
            field=models.ManyToManyField(through='bangregister.Like', to=settings.AUTH_USER_MODEL),
        ),
    ]
