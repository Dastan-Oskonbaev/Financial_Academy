from config.settings import RETAILCRM_URL, RETAILCRM_KEY
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.academy.models import Request
import retailcrm


@receiver(post_save, sender=Request)
def create_crm_order(sender, instance, created, **kwargs):
    try:
        client = retailcrm.v3(RETAILCRM_URL, RETAILCRM_KEY)
        name_parts = instance.full_name.split()
        order = {
            "firstName": name_parts[0] if len(name_parts) > 0 else "",
            "lastName": name_parts[1] if len(name_parts) > 1 else "",
            "patronymic": name_parts[2] if len(name_parts) > 2 else "",
            "phone": instance.phone_number,
            "email": instance.email,
            "orderMethod": "call-request",
        }
        client.order_create(order)
    except Exception as e:
        print("Ошибка при отправке запроса к RetailCRM:", e)
