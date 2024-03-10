from django.db.models.signals import post_save
from django.dispatch import receiver
from libraryapp.models import Jobs

@receiver(post_save, sender=Jobs)
def jobcreated(sender, instance, created, **kwargs):
   if created:
      print('A new job was created', instance.jobid)