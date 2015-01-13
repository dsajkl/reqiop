
from django.db import models
#from django.contrib.auth.models import User
#from django.core.urlresolvers import reverse

# Create your models here.


#from django.db import models

# Create your models here.
class ParentData(models.Model):
        

        ParentName = models.CharField(max_length = 255)
        ParentEmail = models.CharField(max_length = 255)
       
        def __unicode__(self):
                return self.ParentEmail


class P_Data(models.Model):
        studentid = models.BigIntegerField()
        studentemail = models.CharField(max_length = 255)
        parentname = models.CharField(max_length = 255)
        parentemail = models.CharField(max_length = 255)
        parentphone = models.BigIntegerField()
        def __unicode__(self):
                return self.studentemail
