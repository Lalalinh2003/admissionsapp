from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.utils import timezone
from datetime import datetime

# Create your models here.

class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m')
    isCandidate = models.BooleanField(default=False)
    isAdviser = models.BooleanField(default=False)


class Faculty(BaseModel):   #Khoa
    class Meta:
        ordering = ["-id"]

    name = models.CharField(max_length=50, null=False)
    website = models.CharField(max_length=30, blank=True)
    video = models.FileField(null=True, blank=True)
    introduction = RichTextField(null=True, blank=True)
    program = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='faculty/%Y/%m', default=None)

    def __str__(self):
        return self.name


class Major(BaseModel):  #Nganh
    class Meta:
        ordering = ["id"]

    code = models.CharField(max_length=20, unique=True, null=False)
    name = models.CharField(max_length=70, null=False)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, related_name="majors")   #Khoa ngoai voi Faculty
    years = models.ManyToManyField("Year", through="Mark", blank=True)

    def __str__(self):
        return self.name


class Year(BaseModel):  #Nam
    class Meta:
        ordering = ["id"]
    year = models.IntegerField()
    majors = models.ManyToManyField("Major", through="Mark", blank=True)

    def __str__(self):
        return str(self.year)


class Mark(BaseModel):  #Diem
    class Meta:
        ordering = ["id"]
    mark = models.FloatField()
    major = models.ForeignKey(Major, on_delete=models.CASCADE, default=None, related_name="majorfk", blank=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, default=None, related_name="yearfk", blank=True)

    def __str__(self):
        return str(self.mark)


class InformationSection(BaseModel): #Phan thong tin
    class Meta:
        ordering = ["id"]
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Information(BaseModel):  #Thong tin
    class Meta:
        ordering = ["id"]
    infosection = models.ForeignKey(InformationSection, related_name="infos", on_delete=models.SET_NULL, null=True) #Khoa ngoai voi InformationSection
    title = RichTextField(null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to="information/%Y/%m", default=None)

    def __str__(self):
        return self.title


class Comments(BaseModel):  #Binh luan
    class Meta:
        ordering = ["id"]
    content = models.TextField(null=True)
    time = models.DateTimeField(default=datetime.now())
    info = models.ForeignKey(Information, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class BannerImage(BaseModel):  #Anh banner gioi thieu
    image = models.ImageField(upload_to="bannerimages/%Y%m", null=True)


class Livestream(BaseModel):
    announce = models.TextField(blank=True, null=True)   #thong bao
    title = models.TextField(blank=True, null=True)   #tieu de
    time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title


class Questions(BaseModel): #Cau hoi
    class Meta:
        ordering = ["id"]
    content = models.TextField(null=True)
    time = models.DateTimeField(default=datetime.now())
    livestream = models.ForeignKey(Livestream, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class UniversityInfo(BaseModel):  #Thong tin truong
    introduction = RichTextField(blank=True, null=True)











