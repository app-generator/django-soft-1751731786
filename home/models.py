# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class About(models.Model):

    #__About_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(max_length=255, null=True, blank=True)

    #__About_FIELDS__END

    class Meta:
        verbose_name        = _("About")
        verbose_name_plural = _("About")


class Vision(models.Model):

    #__Vision_FIELDS__
    headline = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(max_length=255, null=True, blank=True)

    #__Vision_FIELDS__END

    class Meta:
        verbose_name        = _("Vision")
        verbose_name_plural = _("Vision")


class Service(models.Model):

    #__Service_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    icon = models.CharField(max_length=255, null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)

    #__Service_FIELDS__END

    class Meta:
        verbose_name        = _("Service")
        verbose_name_plural = _("Service")


class Contactmessage(models.Model):

    #__Contactmessage_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(max_length=255, null=True, blank=True)
    sent_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Contactmessage_FIELDS__END

    class Meta:
        verbose_name        = _("Contactmessage")
        verbose_name_plural = _("Contactmessage")


class Blogpost(models.Model):

    #__Blogpost_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    slug = models.TextField(max_length=255, null=True, blank=True)
    content = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Blogpost_FIELDS__END

    class Meta:
        verbose_name        = _("Blogpost")
        verbose_name_plural = _("Blogpost")


class Testimonial(models.Model):

    #__Testimonial_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(max_length=255, null=True, blank=True)

    #__Testimonial_FIELDS__END

    class Meta:
        verbose_name        = _("Testimonial")
        verbose_name_plural = _("Testimonial")



#__MODELS__END
