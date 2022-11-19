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
    workEmail = models.EmailField(max_length=50, unique=True, default="noemail@gmailcom")
    password = models.CharField(max_length=100, null=False, blank=False, )
    photo = models.ImageField(upload_to="photos/profilePictures", null=True, blank=True, max_length=200)

    class Meta:
        abstract = True
        ordering = ['name', 'familyName']


class Portfolio(models.Model):
    class Meta:
        db_table = "Portfolios"


class PersonalInfo(models.Model):
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    PhoneNumber = models.IntegerField(max_length=100, default="no number")
    birthDate = models.DateField(default=date(2003, 1, 1))
    personaEmail = models.EmailField(max_length=50, unique=True, default="noemail@gmailcom")
    personalWebsite = models.URLField(max_length=200)
    linkedinProfile = models.URLField(max_length=200)
    facebookProfile = models.URLField(max_length=200)
    Portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)


class Awards(models.Model):
    Title = models.CharField(max_length=100, null=False, blank=False)
    AwardDate = models.DateField(default=date(2003, 1, 1))
    Justification = models.FileField(upload_to="files/justifications", null=True, blank=True, max_length=200)
    Level = models.CharField(max_length=100, choices=RecognitionLevel,
                             default=RecognitionLevel.Low)
    Portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)


class Transcripts(models.Model):
    Title = models.CharField(max_length=100, null=False, blank=False)
    Description = models.CharField(max_length=100, null=False, blank=False)
    Link = models.URLField(max_length=200)


class Experiences(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(max_length=100, choices=AccomplishmentCategory.choices,
                                default=AccomplishmentCategory.junior)
    StartDate = models.DateField(default=date(2003, 1, 1))
    EndDate = models.DateField(default=date(2003, 1, 1))
    justification = models.FileField(upload_to="files/justifications", null=True, blank=True, max_length=200)
    Portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)


class User(Person):
    jobTitle = models.CharField(max_length=100, default="Unemployed")
    description = models.CharField(max_length=100, default="No description")
    statement = models.CharField(max_length=100, default="No statement ")
    portfolio = models.OneToOneField(Portfolio, on_delete=models.CASCADE)

    class Meta:
        db_table = "Users"
