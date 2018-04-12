from django.db import models
from django.forms import ModelForm


# Create your models here.
# doctor table
class user(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=128)
    levels = models.CharField(max_length=32)
    permission = models.IntegerField()
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-c_time"]
        verbose_name = "User"
        verbose_name_plural = "Users"


class hospital(models.Model):
    hosname = models.CharField(max_length=80)
    def __str__(self):
        return self.hosname    
        
# equipment table

    
class report(models.Model):
    examnum = models.CharField(null = True, max_length=32, verbose_name="EXAM ID")
    name = models.CharField(max_length=50,verbose_name="NAME")
    sex = models.CharField(max_length=32,verbose_name="GENDER")
    age = models.CharField(max_length=32, verbose_name="AGE")
    ageunit = models.CharField(max_length=32)
    examtype = models.CharField(max_length=32,verbose_name="EXAM TYPE")
    position = models.CharField(max_length=80,verbose_name="EXAM POSITION")
    method = models.CharField(max_length=80,verbose_name="EXAM METHOD")
    hospital = models.CharField(max_length=80, verbose_name="HOSPITAL")
    indication = models.CharField(null = True, blank= True, max_length=150,verbose_name="INDICATION")
    findings = models.TextField(verbose_name="FINDINGS")
    comments = models.TextField(null = True, blank= True,verbose_name="COMMENTS")
    examdate = models.CharField(max_length=50,verbose_name="EXAM DATE")
    reportdate = models.CharField(max_length=50,verbose_name="REPORT DATE")
    c_time = models.DateTimeField(auto_now_add=True)
    repdoctor = models.CharField(max_length=50,verbose_name="REPORT DOCTOR")
    status = models.CharField(null = True, blank= True, max_length=32,verbose_name="REPORT STATUS")

    class Meta:
        ordering = ["-c_time"]
    
    def __str__(self):
        return '%s--%s--%s--%s--%s--%s--%s--%s--%s--%s--%s--%s--%s--%s' % (self.examnum, self.name, self.sex, self.age + self.ageunit , self.examtype , self.position, self. method, self.examdate, self.indication, self.findings, self.comments, self.repdoctor, self.reportdate, self.status)


        

# templates table
class reptemplates(models.Model):
    repname = models.CharField(max_length=50)
    findings = models.CharField(max_length=1200)
    comments = models.CharField(max_length=400)
    owner = models.ForeignKey(user,models.SET_NULL,blank=True,null=True,)
        
    def __str__(self):
        return self.repname

