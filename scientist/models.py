from django.db import models


def scientist_image_upload_location(instance, filename):
    return "Scientist/{0}/{1}".format(instance.name, filename)


# Create your models here.
class Scientist(models.Model):
    name = models.CharField(max_length=255, unique=True)
    designation = models.CharField(max_length=255)
    image = models.ImageField(upload_to=scientist_image_upload_location,
                              blank=True, null=True)
    born_and_died = models.CharField(max_length=255)
    address = models.CharField(max_length=500, blank=True, null=True)
    about_him = models.TextField(blank=True, null=True)
    about_his_work = models.TextField(blank=True, null=True)
    work_related_image = models.ImageField(upload_to=scientist_image_upload_location,
                                           blank=True, null=True)
    famous_work_1 = models.TextField(blank=True, null=True)
    image_of_famous_work_1 = models.ImageField(upload_to=scientist_image_upload_location,
                                             blank=True, null=True)
    work_2 = models.TextField(blank=True, null=True)
    image_of_work_2 = models.ImageField(upload_to=scientist_image_upload_location,
                                        blank=True, null=True)
    work_3 = models.TextField(blank=True, null=True)
    image_of_work_3 = models.ImageField(upload_to=scientist_image_upload_location,
                                        blank=True, null=True)
    famous_book_1 = models.TextField(blank=True, null=True)
    image_of_famous_book_1 = models.ImageField(upload_to=scientist_image_upload_location,
                                               blank=True, null=True)
    famous_book_2 = models.TextField(blank=True, null=True)
    image_of_famous_book_2 = models.ImageField(upload_to=scientist_image_upload_location,
                                               blank=True, null=True)
    famous_book_3 = models.TextField(blank=True, null=True)
    image_of_famous_book_3 = models.ImageField(upload_to=scientist_image_upload_location,
                                               blank=True, null=True)
    award_1 = models.CharField(max_length=255, blank=True, null=True)
    award_2 = models.TextField(max_length=255, blank=True, null=True)
    award_3 = models.TextField(max_length=255, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
