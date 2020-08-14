
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from artworks.models import Artwork
# from profiles.models import UserProfile

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_payment_intent_succeeded(self, event):
        """
        Handle a successful payment webhook event
        """
        intent = event.data.object
        print(intent)
        
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle a failed payment webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)