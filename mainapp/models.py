from __future__ import unicode_literals

from django.db import models
from fbstats.users.models import User
from django.db.models import JSONField
#from django.contrib.postgres.fields import JSONField
from model_utils.models import TimeStampedModel
from .manager import *

# Create your models here.


class PSYPT(models.Model):
    """Personality Test Category."""
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(null=False, blank=False)
    short_desc = models.TextField(null=True, blank=True)
    ctitation = models.TextField(null=True, blank=True)
    totalquestions = models.IntegerField(default=20)

    # manager
    objects = PSYPTManager()

    def __str__(self):
        return str(self.name)


class PSYPTDomain(models.Model):
    """Definition for the setup of the test including test identifier and test item identifier."""
    id = models.BigAutoField(primary_key=True)
    psy_pt = models.ForeignKey(PSYPT, on_delete=models.CASCADE)

    domain = models.TextField(null=True, blank=True)
    short_desc = models.TextField(null=False, blank=False)
    long_desc = models.TextField(null=True, blank=True)
    count = models.IntegerField(default=0)

    # manager
    objects = PSYPTDomainManager()
    
    def __str__(self):
        return str(self.domain) + " - " + str(self.psy_pt.name)


class PSYPTFacet(models.Model):
    """Definition for the setup of the test including test identifier and test item identifier."""
    id = models.BigAutoField(primary_key=True)
    psy_pt_domain = models.ForeignKey(PSYPTDomain, on_delete=models.CASCADE)

    facet = models.TextField(null=True, blank=True)
    short_desc = models.TextField(null=False, blank=False)
    long_desc = models.TextField(null=True, blank=True)

    # manager
    objects = PSYPTFacetManager()
    
    def __str__(self):
        return ""


class PSYPTItem(models.Model):
    """Personality Test Item."""
    id = models.BigAutoField(primary_key=True)
    # Foregin key to PSY_PT_DOMAIN
    psy_pt_domain = models.ManyToManyField(PSYPTDomain)

    content = models.TextField(null=False, blank=False)

    # IPIP item number
    item_num_1 = models.TextField(null=False, blank=False)
    
    # IPIP item number
    item_num_2 = models.TextField(null=True, blank=True)
    
    # IPIP item number
    item_num_3 = models.TextField(null=True, blank=True)

    facet = models.TextField(null=True, blank=True)

    # Flag for scoring, e.g. +/-
    keyed = models.TextField(default="+", null=True, blank=True)

    # manager
    objects = PSYPTItemManager()
        
    def __str__(self):
        return str(self.content)


class PSYPTHist(TimeStampedModel):
    """History for Personality Test."""
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    score = models.IntegerField(default=0)

    # manager
    objects = PSYPTHistManager()

    def __str__(self):
        return str(self.score)


class PSYPTUserAttempt(TimeStampedModel):
    """Definition for the test result."""
    id = models.BigAutoField(primary_key=True)
    # test
    test = models.ForeignKey(PSYPTHist, on_delete=models.CASCADE)

    # item
    psy_pt_item = models.ForeignKey(PSYPTItem, on_delete=models.CASCADE)

    # user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # answer text
    answer = models.TextField(null=True, blank=True)

    # manager
    objects = PSYPTUserAttemptManager()
    
    def __str__(self):
        return str(self.psy_pt_item)


class PSYPTResultDef(models.Model):
    """Definition for the test result."""
    id = models.BigAutoField(primary_key=True)
    # Low, neutral, high
    score = models.TextField()

    # Test Descriptipn
    score_desc = models.TextField(null=True, blank=True)

    # Foreigin Key to PSYPTDomain
    psy_pt_domain =  models.ForeignKey(PSYPTDomain, on_delete=models.CASCADE)

    # manager
    objects = PSYPTResultDefManager()
    
    def __str__(self):
        return str(self.score)



    
