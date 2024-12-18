# Generated by Django 4.2.16 on 2024-11-27 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Number",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.CharField(max_length=32, verbose_name="手机号")),
                ("price", models.IntegerField(verbose_name="价格")),
                (
                    "level",
                    models.SmallIntegerField(
                        choices=[(1, "普通用户"), (2, "VIP")],
                        default=1,
                        verbose_name="用户等级",
                    ),
                ),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[(1, "未售"), (2, "已售")], default=1, verbose_name="状态"
                    ),
                ),
            ],
        ),
    ]
