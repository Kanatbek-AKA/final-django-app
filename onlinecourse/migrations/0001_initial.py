# Generated by Django 4.1.7 on 2023-03-05 22:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('choice_answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=200)),
                ('answer', models.CharField(default='write your answer', max_length=200)),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='online course', max_length=30)),
                ('image', models.ImageField(upload_to='course_images/')),
                ('description', models.CharField(max_length=1000)),
                ('pub_date', models.DateField(null=True)),
                ('total_enrollment', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_enrolled', models.DateField(default=django.utils.timezone.now)),
                ('mode', models.CharField(choices=[('audit', 'Audit'), ('honor', 'Honor'), ('BETA', 'BETA')], default='audit', max_length=5)),
                ('rating', models.FloatField(default=5.0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('choices', models.ManyToManyField(to='onlinecourse.choice')),
                ('enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.enrollment')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question_text', models.CharField(max_length=200)),
                ('grade', models.FloatField(default=1.0)),
                ('lesson', models.ManyToManyField(to='onlinecourse.course')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='title', max_length=200)),
                ('order', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course')),
            ],
        ),
        migrations.CreateModel(
            name='Learner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('occupation', models.CharField(choices=[('student', 'Student'), ('developer', 'Developer'), ('data_scientist', 'Data Scientist'), ('dba', 'Database Admin')], default='student', max_length=20)),
                ('social_link', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_time', models.BooleanField(default=True)),
                ('total_learners', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='examGrades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course')),
                ('exam_answer', models.ManyToManyField(to='onlinecourse.choice')),
                ('exam_question', models.ManyToManyField(to='onlinecourse.question')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='instructors',
            field=models.ManyToManyField(to='onlinecourse.instructor'),
        ),
        migrations.AddField(
            model_name='course',
            name='users',
            field=models.ManyToManyField(through='onlinecourse.Enrollment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.question'),
        ),
    ]
