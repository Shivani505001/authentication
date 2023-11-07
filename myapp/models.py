from django.db import models
from django.core.validators import RegexValidator,MinLengthValidator
 
roll_number_regex = RegexValidator(
        regex=r'^[A-Z]{2}\d{3}$',  # This regex enforces two uppercase letters followed by three digits.
        message="Roll number must consist of two uppercase letters followed by three digits."
    )
phone_regex = RegexValidator(
    regex=r'^\d{10}$',
    message="Phone number must be exactly 10 digits.",
)

class User(models.Model):
    name = models.CharField(max_length=100)
   
    roll_number = models.CharField(
        validators=[roll_number_regex],
        max_length=5,
        unique=True,
    )
    password = models.CharField(
        validators=[MinLengthValidator(8)],
        max_length=128,
    )  # Store hashed passwords, use a better hashing method in production
    
    phone_number = models.CharField(max_length=10, validators=[phone_regex])

    def __str__(self):
        return self.name
