from datetime import date

from django.db import models


# Create your models here.

# Enum
class AccomplishmentCategory(models.TextChoices):
    senior = "senior"
    junior = "junior"


class AwardType(models.TextChoices):
    honor = "honor"
    scholarship = "scholarship"
    award = "award"


class RecognitionLevel(models.TextChoices):
    High = "High"
    Mid = "Mid"
    Low = "Low"


class Address(models.Model):
    number = models.FloatField(default=0.0)
    streetName = models.CharField(max_length=50, default="no  street name")
    Postalcode = models.IntegerField(default=0)
    city = models.CharField(max_length=50, default="no  city name")

    class Meta:
        db_table = "Address"


class Person(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, default="no name")
    familyName = models.CharField(max_length=100, null=False, blank=False, default="no family name")
    email = models.EmailField(max_length=50, unique=True, default="noemail@gmailcom")
    photo = models.ImageField(upload_to="photos/profilePictures", null=True, blank=True, max_length=200)

    class Meta:
        abstract = True
        ordering = ['name', 'familyName']


class User(Person):
    jobTitle = models.CharField(max_length=100, default="Unemployed")
    description = models.CharField(max_length=100, default="No description")
    password = models.CharField(max_length=100,default="PasswordDefault")
    statement = models.CharField(max_length=100, default="No statement ")

    class Meta:
        db_table = "Users"


class Admin(Person):
    specialKey = models.CharField(max_length=100, null=False, blank=False, )

    class Meta:
        db_table = "Admins"


class PersonalInfo(models.Model):
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    PhoneNumber = models.IntegerField(default="no number")
    birthDate = models.DateField(default=date(2003, 1, 1))
    personaEmail = models.EmailField(max_length=50, unique=True, default="noemail@gmailcom")
    personalWebsite = models.URLField(max_length=200)
    linkedinProfile = models.URLField(max_length=200)
    facebookProfile = models.URLField(max_length=200)
    User = models.OneToOneField(User, on_delete=models.CASCADE)


class Awards(models.Model):
    Title = models.CharField(max_length=100, null=False, blank=False)
    AwardDate = models.DateField(default=date(2003, 1, 1))
    Justification = models.FileField(upload_to="files/justifications", null=True, blank=True, max_length=200)
    Level = models.CharField(max_length=100, choices=RecognitionLevel.choices,
                             default=RecognitionLevel.Low)
    User = models.ForeignKey(User, on_delete=models.CASCADE)


class Transcripts(models.Model):
    Title = models.CharField(max_length=100, null=False, blank=False)
    Description = models.CharField(max_length=100, null=False, blank=False)
    Link = models.URLField(max_length=200)
    User = models.ForeignKey(User, on_delete=models.CASCADE)


class Experiences(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(max_length=100, choices=AccomplishmentCategory.choices,
                                default=AccomplishmentCategory.junior)
    StartDate = models.DateField(default=date(2003, 1, 1))
    EndDate = models.DateField(default=date(2003, 1, 1))
    justification = models.FileField(upload_to="files/justifications", null=True, blank=True, max_length=200)
    User = models.ForeignKey(User, on_delete=models.CASCADE)


class References(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, default="no name")
    familyName = models.CharField(max_length=100, null=False, blank=False, default="no family name")
    PhoneNumber = models.IntegerField(default="no number")
    personaEmail = models.EmailField(max_length=50, unique=True, default="noemail@gmailcom")
    title = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(max_length=100, choices=AccomplishmentCategory.choices,
                                default=AccomplishmentCategory.junior)
    justification = models.FileField(upload_to="files/justifications")
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "References"


class Volunteering(models.Model):
    label = models.CharField(max_length=100, null=False, blank=False, default="no label")
    description = models.CharField(max_length=250, null=False, blank=False, default="no description")
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Volunteering"
