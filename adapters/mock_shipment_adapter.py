from domain.ports.shipment_port import ShipmentPort
from typing import Any, Dict

class MockShipmentAdapter(ShipmentPort):
    def __init__(self):
        self.shipments = {}

    def create_shipment(self, order_id: str, recipient_name: str, recipient_address: str) -> Dict[str, Any]:
        self.order_id = order_id
        self.recipient_name = recipient_name
        self.recipient_address = recipient_address
        shipment = {
            "order_id": self.order_id,
            "recipient_name": self.recipient_name,
            "recipient_address": self.recipient_address,
            "tracking_number": "9261290312833844954982",
            "courier_code": "usps",
            "status": "Created"
        }
        self.shipments[order_id] = shipment
        return shipment

    def get_shipment_status(self, order_id: str) -> Dict[str, Any]:
        shipment = self.shipments.get(order_id)
        if shipment:
            return {"order_id": order_id, "status": shipment["status"]}
        else:
            return {"error": "Shipment not found"}

    def cancel_shipment(self, order_id: str) -> Dict[str, Any]:
        shipment = self.shipments.get(order_id)
        if shipment:
            shipment["status"] = "Cancelled"
            return {"order_id": order_id, "status": "Cancelled"}
        else:
            return {"error": "Shipment not found"}

    def tracking_shipment(self, tracking_number: int) -> Dict[str, Any]:
        self.tracking_number = tracking_number
        tracking = {
            "id": "02f1e5eb4d9fae6a91d839549b7dcf6d",
            "tracking_number": self.tracking_number,
            "courier_code": "usps",
            "order_number": self.tracking_number,
            "order_date": None,
            "created_at": "2023-11-15T06:07:40+00:00",
            "update_at": "2024-01-03T06:18:46+00:00",
            "delivery_status": "created",
            "archived": "tracking",
            "updating": False,
            "source": "WEB",
            "destination_country": None,
            "destination_state": "SC",
            "destination_city": "HEMINGWAY",
            "origin_country": "US",
            "origin_state": "FL",
            "origin_city": "FORT LAUDERDALE",
            "tracking_postal_code": None,
            "tracking_ship_date": None,
            "tracking_destination_country": None,
            "tracking_origin_country": None,
            "tracking_key": None,
            "tracking_courier_account": None,
            "customer_name": None,
            "customer_email": None,
            "customer_sms": None,
            "recipient_postcode": None,
            "order_id": None,
            "title": None,
            "logistics_channel": None,
            "note": None,
            "label": "1,2",
            "signed_by": None,
            "service_code": None,
            "weight": None,
            "weight_kg": None,
            "product_type": None,
            "pieces": None,
            "dimension": None,
            "previously": None,
            "destination_track_number": None,
            "exchange_number": None,
            "scheduled_delivery_date": None,
            "scheduled_address": None,
            "substatus": "created",
            "status_info": None,
            "latest_event": None,
            "latest_checkpoint_time": None,
            "transit_time": 0,
            "origin_info": {
                "courier_code": None,
                "courier_phone": None,
                "weblink": "https://www.usps.com/",
                "reference_number": None,
                "milestone_date": {
                    "inforeceived_date": None,
                    "pickup_date": None,
                    "outfordelivery_date": None,
                    "delivery_date": None,
                    "returning_date": None,
                    "returned_date": None
                },
                "pickup_date": None,
                "departed_airport_date": None,
                "arrived_abroad_date": None,
                "customs_received_date": None,
                "trackinfo": []
            },
            "destination_info": {
                "courier_code": None,
                "courier_phone": None,
                "weblink": None,
                "reference_number": None,
                "milestone_date": {
                    "inforeceived_date": None,
                    "pickup_date": None,
                    "outfordelivery_date": None,
                    "delivery_date": None,
                    "returning_date": None,
                    "returned_date": None
                },
                "pickup_date": None,
                "departed_airport_date": None,
                "arrived_abroad_date": None,
                "customs_received_date": None,
                "trackinfo": []
            },
            "substatusV2": None,
            "substatusTimeV2": None,
            "stausDataNumV2": None
        }
        return tracking
