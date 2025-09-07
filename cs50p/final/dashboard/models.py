from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
  pass

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
  content = models.TextField()
  amount = models.IntegerField(default=0, null=True, blank=True)
  id = models.AutoField(primary_key=True)
  color = models.CharField(max_length=7, default='#4e73df')
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.user.username}: {self.content} at {self.created_at.strftime('%d-%m-%Y %H:%M')}"

class Transaction(models.Model):
    INCOME = 'IN'
    EXPENSE = 'EX'
    TRANSACTION_TYPE_CHOICES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=2, choices=TRANSACTION_TYPE_CHOICES)
    description = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.get_transaction_type_display()} of {self.amount}"