# Generated by Django 5.1.6 on 2025-02-18 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course_app", "0002_alter_course_options_alter_course_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tutor",
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
                ("name", models.CharField(max_length=50)),
                ("familyName", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("birthdate", models.DateField()),
                (
                    "photo",
                    models.ImageField(
                        blank=True, null=True, upload_to="images/tutor_avatars/"
                    ),
                ),
                (
                    "grade",
                    models.CharField(
                        choices=[
                            ("Assistant", "Asst"),
                            ("Associate", "Assoc"),
                            ("Professor", "Prof"),
                            ("Expert", "Expr"),
                        ],
                        default="Assistant",
                        max_length=50,
                    ),
                ),
            ],
            options={
                "db_table": "tutors",
                "ordering": ["name", "familyName"],
            },
        ),
        migrations.AlterField(
            model_name="course",
            name="courseAvatar",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/course_avatars/"
            ),
        ),
    ]
