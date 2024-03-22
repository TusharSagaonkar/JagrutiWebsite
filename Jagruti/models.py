from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
import os

def employee_image_path(instance, filename):
    upload_to = 'images/'
    ext = filename.split('.')[-1]
    name = "%s_%s" % (instance.name.replace(" ", "_"), instance.designation.replace(" ", "_"))
    new_filename = f"{name}.{ext}"
    if os.path.exists(os.path.join(upload_to, new_filename)):
        # Find the next available number
        index = 1
        while os.path.exists(os.path.join(upload_to, f"{name}_{index}.{ext}")):
            index += 1
        new_filename = f"{name}_{index}.{ext}"
    return os.path.join(upload_to, new_filename)

class Employee(models.Model):
  LEVEL_CHOICES = [(i, f'Level {i}') for i in range(1, 15)]  # Updated choices from 1 to 50
  name = models.CharField(max_length=100)
  designation = models.CharField(max_length=100)
  level = models.IntegerField(choices=LEVEL_CHOICES, default=1)
  image = models.ImageField(upload_to=employee_image_path)

  def __str__(self):
      return self.name

@receiver(pre_delete, sender=Employee)
def employee_pre_delete(sender, instance, **kwargs):
    # Delete associated image when employee is deleted
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(pre_save, sender=Employee)
def employee_pre_save(sender, instance, **kwargs):
    if instance.pk:  # If the instance has already been saved (i.e., it's being updated)
        try:
            old_instance = Employee.objects.get(pk=instance.pk)
            if old_instance.image != instance.image:  # If the image has changed
                if old_instance.image:  # If there was a previous image
                    if os.path.isfile(old_instance.image.path):
                        os.remove(old_instance.image.path)  # Delete the previous image file
        except Employee.DoesNotExist:
            pass  # No previous instance found or instance being created, do nothing

class SocietyInformation(models.Model):
    data_heading = models.CharField(max_length=100, blank=False, null=False)
    detail_info = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.data_heading

from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from datetime import datetime
import os

def file_upload_path(instance, filename):
      # Define the upload path for the file
      return f"uploads/{datetime.now().strftime('%Y/%m/%d')}/{filename}"

class UploadedFile(models.Model):
      name = models.CharField(max_length=255)
      upload_date = models.DateTimeField(auto_now_add=True)
      file = models.FileField(upload_to=file_upload_path)

      def __str__(self):
          return self.name

@receiver(pre_delete, sender=UploadedFile)
def uploaded_file_pre_delete(sender, instance, **kwargs):
      # Delete associated file when UploadedFile instance is deleted
      if instance.file:
          if os.path.isfile(instance.file.path):
              os.remove(instance.file.path)




class Scheme(models.Model):
    scheme_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.scheme_name

class Tenure(models.Model):
    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE, related_name='tenures')
    tenure = models.CharField(max_length=100)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('scheme', 'tenure')

    def __str__(self):
        return f"{self.tenure} ({self.interest_rate}%)"
