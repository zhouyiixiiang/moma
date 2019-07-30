from django.db import models
from tinymce.models import HTMLField


class TypeInfo(models.Model):
    ttitle=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)
    def __str__(self):
        return self.ttitle

class booksinfo(models.Model):
    bauthor = models.CharField(max_length=50)
    bpress=models.CharField(max_length=50)
    btitle=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=20)
    original_title=models.CharField(max_length=50)
    translator=models.CharField(max_length=20)
    #publication_date=models.DateField()
    publication_date = models.CharField(max_length=20)
    number_of_pages=models.IntegerField()
    bprice = models.CharField(max_length=50)
    bscore= models.DecimalField(max_digits=3, decimal_places=1)
    popularity=models.DecimalField(max_digits=7, decimal_places=0)
    content_validity=HTMLField()
    introduction_to_author=HTMLField()
    #gclick = models.IntegerField()
    tags=models.CharField(max_length=50)
    bpic=models.ImageField(upload_to='static/books',default='')
    #bfile_mobi=models.FileField(upload_to='file_mobi',default='')
    #bfile_azw3 = models.FileField(upload_to='file_azw3',default='')
    #bfile_epub = models.FileField(upload_to='file_epub',default='')
    #bfile_pdf = models.FileField(upload_to='file_pdf',default='')
    #bfile_txt = models.FileField(upload_to='file_txt',default='')
    #gprice=models.DecimalField(max_digits=5,decimal_places=2)
    #gclick=models.IntegerField()
    #gtype=models.ForeignKey(TypeInfo,on_delete=models.CASCADE)
    #isDelete=models.BooleanField(default=False)



