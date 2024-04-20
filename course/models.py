from django.db import models
from .helpers import SaveMediaFiles,Choises

class Speciality(models.Model):
    title = models.CharField(max_length=25)
    image = models.ImageField(upload_to=SaveMediaFiles.speciality_image_path)
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.title}'

class About(models.Model):
    title = models.CharField(max_length=25)
    image = models.ImageField(upload_to='course/about/')
    description = models.TextField()

    def __str__(self):
        return self.title

class Course(models.Model):


    title = models.CharField(max_length=30)
    slug = models.SlugField(verbose_name='Slug', max_length=255)
    image = models.ImageField(upload_to=SaveMediaFiles.speciality_image_path)
    description = models.TextField()
    active_users = models.PositiveIntegerField(default=0)
    price = models.FloatField()
    price_type = models.CharField(max_length=12, choices=Choises.PriceType.choices, default=Choises.PriceType.d)
    reting = models.FloatField(null=True)
    status = models.CharField(max_length=25, choices=Choises.CourseStatus.choices, default=Choises.CourseStatus.DRAFT)
    speciality = models.ManyToManyField(Speciality)
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title


class Position(models.Model):
    name = models.CharField(max_length=100)
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='course/teacher/')
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    x_link = models.URLField(null=True, blank=False)
    m_link = models.URLField(null=True, blank=False)
    l_link = models.URLField(null=True, blank=False)
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)


    def full_name(self):
        return f'{self.first_name} {self.last_name}'


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

