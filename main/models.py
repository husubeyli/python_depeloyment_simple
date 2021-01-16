from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class Account(models.Model):
    first_name = models.CharField(_('Name'), max_length=30, db_index=True)
    last_name = models.CharField(_('Surname'), max_length=50, db_index=True)
    email = models.EmailField(_('email address'), unique=True)

    # moderations
    is_published = models.BooleanField(_('is published'), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')
        # ordering = ('-created_at')

    def __str__(self):
        return self.first_name