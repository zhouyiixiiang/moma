# Generated by Django 2.0.2 on 2018-09-08 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_books', '0005_auto_20180909_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksinfo',
            name='bfile_azw3',
            field=models.FileField(default='', upload_to='file_azw3'),
        ),
        migrations.AlterField(
            model_name='booksinfo',
            name='bfile_epub',
            field=models.FileField(default='', upload_to='file_epub'),
        ),
        migrations.AlterField(
            model_name='booksinfo',
            name='bfile_mobi',
            field=models.FileField(default='', upload_to='file_mobi'),
        ),
        migrations.AlterField(
            model_name='booksinfo',
            name='bfile_pdf',
            field=models.FileField(default='', upload_to='file_pdf'),
        ),
        migrations.AlterField(
            model_name='booksinfo',
            name='bfile_txt',
            field=models.FileField(default='', upload_to='file_txt'),
        ),
        migrations.AlterField(
            model_name='booksinfo',
            name='bpic',
            field=models.ImageField(default='', upload_to='static/books'),
        ),
    ]