from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # will store hashed password
    mobile_number = models.CharField(max_length=15, unique=True)
    address = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)  # optional
    updated_at = models.DateTimeField(auto_now=True)      # optional

    class Meta:
        db_table = "users"   # custom table name

    def __str__(self):
        return self.name