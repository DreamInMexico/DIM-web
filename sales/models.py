from __future__ import unicode_literals

from django.db import models
from django.conf import settings
import conekta
import json

class Sale(models.Model):
    def __init__(self, *args, **kwargs):
        super(Sale, self).__init__(*args, **kwargs)

        conekta.api_key = settings.CONEKTA_PRIVATE_KEY

    def charge(self, price_in_cents, token_id,name):
        try:
            order = conekta.Order.create({
                "line_items": [
                    {
                        "name": "Boleto de Rifa Dream in Mexico",
                        "description": "Boleto para ganar una bocina.",
                        "unit_price": price_in_cents,
                        "quantity": 1,
                        "sku": "cohb_s1",
                        "category": "tech",
                        "type" : "physical",
                        "tags" : ["food", "mexican food"]
                    }
                ],
                "customer_info":{
                    "name": name,
                    "phone": "+525533445566",
                    "email": "john@meh.com",
                    "corporate": False,
                    "vertical_info": {}
                    },
                
                "fiscal_entity":{
                    "tax_id": "AMGH851205MN1",
                    "name": "Nike SA de CV",
                    "address": {
                        "street1": "250 Alexis St",
                        "internal_number": "19",
                        "external_number": "91",
                        "city": "Red Deer",
                        "state": "Alberta",
                        "country": "CA",
                        "postal_code": "33242"
                    }
                },
                "charges": [{
                    "payment_method":{
                    "type": "card",
                    "token_id": token_id
                    },
                    "amount": price_in_cents
                }],
                "currency" : "mxn",
                "metadata" : {"test" : "extra info"}
                })

        except conekta.ConektaError as e:
            print (e.message)
            #El pago no pudo ser procesado

            #You can also get the attributes from the conekta response class:
        print (order.id)