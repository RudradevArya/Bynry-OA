from django.db import models
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings

User = get_user_model()

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.request_type} - {self.user.username} - {self.status}"

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        old_status = self.status if not is_new else None
        super().save(*args, **kwargs)
        if not is_new and old_status != self.status:
            self.send_status_update_email()

    def send_status_update_email(self):
        subject = f'Service Request Status Update - {self.request_type}'
        message = f'Your service request "{self.request_type}" has been updated to status: {self.get_status_display()}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [self.user.email]
        send_mail(subject, message, from_email, recipient_list)