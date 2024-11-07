from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Location(models.Model):
    """
        Specific venue  or url in case of online event
    """
    location_type = models.CharField(
        max_length=20,
        choices=[('PHYSICAL', 'Physical'), ('ONLINE', 'Online')],
        default='PHYSICAL'
    )
    address = models.CharField(max_length=255, blank=True, null=True, help_text="Address for physical locations")
    url = models.URLField(blank=True, null=True, help_text="URL for online events")

    def __str__(self):
        return self.address if self.location_type == 'PHYSICAL' else self.url#validate that at least one of address or url is not None

class Organizer(models.Model):
    """
        Person or organization responsible for the event
    """
    ORGANIZER_TYPES = [
        ('INDIVIDUAL', 'Individual'),
        ('ORGANIZATION', 'Organization')
    ]
    name = models.CharField(max_length=100)
    organizer_type = models.CharField(max_length=20, choices=ORGANIZER_TYPES, verbose_name="Organizer type")#default = INDIVIDUAL
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=127)
    description = models.TextField()
    date = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="User that registered event", null=True)


    def __str__(self):
        return f"{self.title} at {self.location}. By {self.organizer}"

    def get_absolute_url(self):
        return reverse("event-detail", kwargs={"pk": self.pk})


class Visitor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User that registered this visitor")
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    events = models.ManyToManyField(Event, related_name="visitors")
    