# Generated by Django 3.1.1 on 2020-09-23 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='collage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collagename', models.CharField(default='', max_length=10)),
            ],
            options={
                'db_table': 'collage',
            },
        ),
        migrations.CreateModel(
            name='Registraion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'register',
            },
        ),
        migrations.CreateModel(
            name='TeacherDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teachername', models.CharField(max_length=20)),
                ('teacherphone', models.IntegerField()),
                ('tearcher_email', models.CharField(max_length=100)),
                ('teacher_image', models.ImageField(default='', upload_to='media')),
                ('teach_collage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Collage_id', to='operation.collage')),
            ],
            options={
                'db_table': 'Teacher',
            },
        ),
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=30)),
                ('student_email', models.CharField(max_length=100)),
                ('student_marks', models.CharField(max_length=10)),
                ('student_image', models.ImageField(default='', upload_to='media')),
                ('student_collage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collage_id', to='operation.collage')),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
