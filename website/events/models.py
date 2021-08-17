from django.db import models

# Create your models here.from django.db import models
#
# # Create your models here.
class Guntur(models.Model):
     district = models.CharField(default='',max_length=100)
     num = models.CharField(default=0, max_length=200)
     userid  =  models.CharField(max_length=30, default='')
     n1 = models.CharField(default=0,max_length=200)
     n2 = models.CharField(default=0,max_length=200)
     n3 = models.CharField(default=0,max_length=200)
     n4 = models.CharField(default=0,max_length=200)
     n5 = models.CharField(default=0,max_length=200)
     n6 = models.CharField(default=0,max_length=200)
     n7 = models.CharField(default=0,max_length=200)
     n8 = models.CharField(default=0,max_length=200)
     n9 = models.CharField(default=0,max_length=200)
     n10 = models.CharField(default=0,max_length=200)
     n11 = models.CharField(default=0,max_length=200)
     n12 = models.CharField(default=0,max_length=200)
     n13 = models.CharField(default=0,max_length=200)

     def __str__(self):
          return self.district

class EG(models.Model):
     district = models.CharField(default='',max_length=100)
     num = models.CharField(default=0, max_length=200)
     userid  =  models.CharField(max_length=30, default='')
     n1 = models.CharField(default=0,max_length=200)
     n2 = models.CharField(default=0,max_length=200)
     n3 = models.CharField(default=0,max_length=200)
     n4 = models.CharField(default=0,max_length=200)
     n5 = models.CharField(default=0,max_length=200)
     n6 = models.CharField(default=0,max_length=200)
     n7 = models.CharField(default=0,max_length=200)
     n8 = models.CharField(default=0,max_length=200)
     n9 = models.CharField(default=0,max_length=200)
     n10 = models.CharField(default=0,max_length=200)
     n11 = models.CharField(default=0,max_length=200)
     n12 = models.CharField(default=0,max_length=200)
     n13 = models.CharField(default=0,max_length=200)

     def __str__(self):
          return self.district


class WG(models.Model):
     district = models.CharField(default='', max_length=100)
     num = models.CharField(default=0, max_length=200)
     userid = models.CharField(max_length=30, default='')
     n1 = models.CharField(default=0, max_length=200)
     n2 = models.CharField(default=0, max_length=200)
     n3 = models.CharField(default=0, max_length=200)
     n4 = models.CharField(default=0, max_length=200)
     n5 = models.CharField(default=0, max_length=200)
     n6 = models.CharField(default=0, max_length=200)
     n7 = models.CharField(default=0, max_length=200)
     n8 = models.CharField(default=0, max_length=200)
     n9 = models.CharField(default=0, max_length=200)
     n10 = models.CharField(default=0, max_length=200)
     n11 = models.CharField(default=0, max_length=200)
     n12 = models.CharField(default=0, max_length=200)
     n13 = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.district


class Krishna(models.Model):
     district = models.CharField(default='', max_length=100)
     num = models.CharField(default=0, max_length=200)
     userid = models.CharField(max_length=30, default='')
     n1 = models.CharField(default=0, max_length=200)
     n2 = models.CharField(default=0, max_length=200)
     n3 = models.CharField(default=0, max_length=200)
     n4 = models.CharField(default=0, max_length=200)
     n5 = models.CharField(default=0, max_length=200)
     n6 = models.CharField(default=0, max_length=200)
     n7 = models.CharField(default=0, max_length=200)
     n8 = models.CharField(default=0, max_length=200)
     n9 = models.CharField(default=0, max_length=200)
     n10 = models.CharField(default=0, max_length=200)
     n11 = models.CharField(default=0, max_length=200)
     n12 = models.CharField(default=0, max_length=200)
     n13 = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.district


class Prakasham(models.Model):
     district = models.CharField(default='', max_length=100)
     num = models.CharField(default=0, max_length=200)
     userid = models.CharField(max_length=30, default='')
     n1 = models.CharField(default=0, max_length=200)
     n2 = models.CharField(default=0, max_length=200)
     n3 = models.CharField(default=0, max_length=200)
     n4 = models.CharField(default=0, max_length=200)
     n5 = models.CharField(default=0, max_length=200)
     n6 = models.CharField(default=0, max_length=200)
     n7 = models.CharField(default=0, max_length=200)
     n8 = models.CharField(default=0, max_length=200)
     n9 = models.CharField(default=0, max_length=200)
     n10 = models.CharField(default=0, max_length=200)
     n11 = models.CharField(default=0, max_length=200)
     n12 = models.CharField(default=0, max_length=200)
     n13 = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.district


class Nellore(models.Model):
     district = models.CharField(default='', max_length=100)
     num = models.CharField(default=0, max_length=200)
     userid = models.CharField(max_length=30, default='')
     n1 = models.CharField(default=0, max_length=200)
     n2 = models.CharField(default=0, max_length=200)
     n3 = models.CharField(default=0, max_length=200)
     n4 = models.CharField(default=0, max_length=200)
     n5 = models.CharField(default=0, max_length=200)
     n6 = models.CharField(default=0, max_length=200)
     n7 = models.CharField(default=0, max_length=200)
     n8 = models.CharField(default=0, max_length=200)
     n9 = models.CharField(default=0, max_length=200)
     n10 = models.CharField(default=0, max_length=200)
     n11 = models.CharField(default=0, max_length=200)
     n12 = models.CharField(default=0, max_length=200)
     n13 = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.district


class Chittoor(models.Model):
     district = models.CharField(default='', max_length=100)
     num = models.CharField(default=0, max_length=200)
     userid = models.CharField(max_length=30, default='')
     n1 = models.CharField(default=0, max_length=200)
     n2 = models.CharField(default=0, max_length=200)
     n3 = models.CharField(default=0, max_length=200)
     n4 = models.CharField(default=0, max_length=200)
     n5 = models.CharField(default=0, max_length=200)
     n6 = models.CharField(default=0, max_length=200)
     n7 = models.CharField(default=0, max_length=200)
     n8 = models.CharField(default=0, max_length=200)
     n9 = models.CharField(default=0, max_length=200)
     n10 = models.CharField(default=0, max_length=200)
     n11 = models.CharField(default=0, max_length=200)
     n12 = models.CharField(default=0, max_length=200)
     n13 = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.district


class Visakha(models.Model):
     district = models.CharField(default='', max_length=100)
     num = models.CharField(default=0, max_length=200)
     userid = models.CharField(max_length=30, default='')
     n1 = models.CharField(default=0, max_length=200)
     n2 = models.CharField(default=0, max_length=200)
     n3 = models.CharField(default=0, max_length=200)
     n4 = models.CharField(default=0, max_length=200)
     n5 = models.CharField(default=0, max_length=200)
     n6 = models.CharField(default=0, max_length=200)
     n7 = models.CharField(default=0, max_length=200)
     n8 = models.CharField(default=0, max_length=200)
     n9 = models.CharField(default=0, max_length=200)
     n10 = models.CharField(default=0, max_length=200)
     n11 = models.CharField(default=0, max_length=200)
     n12 = models.CharField(default=0, max_length=200)
     n13 = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.district


class Vizianagaram(models.Model):
     district = models.CharField(default='', max_length=100)
     num = models.CharField(default=0, max_length=200)
     userid = models.CharField(max_length=30, default='')
     n1 = models.CharField(default=0, max_length=200)
     n2 = models.CharField(default=0, max_length=200)
     n3 = models.CharField(default=0, max_length=200)
     n4 = models.CharField(default=0, max_length=200)
     n5 = models.CharField(default=0, max_length=200)
     n6 = models.CharField(default=0, max_length=200)
     n7 = models.CharField(default=0, max_length=200)
     n8 = models.CharField(default=0, max_length=200)
     n9 = models.CharField(default=0, max_length=200)
     n10 = models.CharField(default=0, max_length=200)
     n11 = models.CharField(default=0, max_length=200)
     n12 = models.CharField(default=0, max_length=200)
     n13 = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.district


class Srikakulam(models.Model):
     district = models.CharField(default='', max_length=100)
     num = models.CharField(default=0, max_length=200)
     userid = models.CharField(max_length=30, default='')
     n1 = models.CharField(default=0, max_length=200)
     n2 = models.CharField(default=0, max_length=200)
     n3 = models.CharField(default=0, max_length=200)
     n4 = models.CharField(default=0, max_length=200)
     n5 = models.CharField(default=0, max_length=200)
     n6 = models.CharField(default=0, max_length=200)
     n7 = models.CharField(default=0, max_length=200)
     n8 = models.CharField(default=0, max_length=200)
     n9 = models.CharField(default=0, max_length=200)
     n10 = models.CharField(default=0, max_length=200)
     n11 = models.CharField(default=0, max_length=200)
     n12 = models.CharField(default=0, max_length=200)
     n13 = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.district


class kadapa(models.Model):
     district = models.CharField(default='', max_length=100)
     num = models.CharField(default=0, max_length=200)
     userid = models.CharField(max_length=30, default='')
     n1 = models.CharField(default=0, max_length=200)
     n2 = models.CharField(default=0, max_length=200)
     n3 = models.CharField(default=0, max_length=200)
     n4 = models.CharField(default=0, max_length=200)
     n5 = models.CharField(default=0, max_length=200)
     n6 = models.CharField(default=0, max_length=200)
     n7 = models.CharField(default=0, max_length=200)
     n8 = models.CharField(default=0, max_length=200)
     n9 = models.CharField(default=0, max_length=200)
     n10 = models.CharField(default=0, max_length=200)
     n11 = models.CharField(default=0, max_length=200)
     n12 = models.CharField(default=0, max_length=200)
     n13 = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.district


class Kurnool(models.Model):
     district = models.CharField(default='', max_length=100)
     num = models.CharField(default=0, max_length=200)
     userid = models.CharField(max_length=30, default='')
     n1 = models.CharField(default=0, max_length=200)
     n2 = models.CharField(default=0, max_length=200)
     n3 = models.CharField(default=0, max_length=200)
     n4 = models.CharField(default=0, max_length=200)
     n5 = models.CharField(default=0, max_length=200)
     n6 = models.CharField(default=0, max_length=200)
     n7 = models.CharField(default=0, max_length=200)
     n8 = models.CharField(default=0, max_length=200)
     n9 = models.CharField(default=0, max_length=200)
     n10 = models.CharField(default=0, max_length=200)
     n11 = models.CharField(default=0, max_length=200)
     n12 = models.CharField(default=0, max_length=200)
     n13 = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.district


class Ananthapur(models.Model):
     district = models.CharField(default='', max_length=100)
     num = models.CharField(default=0, max_length=200)
     userid = models.CharField(max_length=30, default='')
     n1 = models.CharField(default=0, max_length=200)
     n2 = models.CharField(default=0, max_length=200)
     n3 = models.CharField(default=0, max_length=200)
     n4 = models.CharField(default=0, max_length=200)
     n5 = models.CharField(default=0, max_length=200)
     n6 = models.CharField(default=0, max_length=200)
     n7 = models.CharField(default=0, max_length=200)
     n8 = models.CharField(default=0, max_length=200)
     n9 = models.CharField(default=0, max_length=200)
     n10 = models.CharField(default=0, max_length=200)
     n11 = models.CharField(default=0, max_length=200)
     n12 = models.CharField(default=0, max_length=200)
     n13 = models.CharField(default=0, max_length=200)

     def __str__(self):
          return self.district
