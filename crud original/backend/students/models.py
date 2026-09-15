from django.core.validators import RegexValidator
from django.db import models


class Student(models.Model):
    class YearOfStudy(models.IntegerChoices):
        FIRST = 1, "1st Year"
        SECOND = 2, "2nd Year"
        THIRD = 3, "3rd Year"
        FOURTH = 4, "4th Year"

    phone_validator = RegexValidator(
        regex=r"^\+?\d{7,15}$",
        message="Enter a valid phone number (7–15 digits, optional leading +).",
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=16, validators=[phone_validator])
    department = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField(choices=YearOfStudy.choices)
    enrollment_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-enrollment_date", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.department})"
