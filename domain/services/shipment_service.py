from typing import Any, Dict
from domain.ports.shipment_port import ShipmentPort

class ShipmentService:
    def __init__(self, shipment_port: ShipmentPort):
        self.shipment_port = shipment_port
    
    def create_shipment(self, order_id: str, recipient_name: str, recipient_address: str) -> Dict[str, Any]:
        return self.shipment_port.create_shipment(order_id, recipient_name, recipient_address)
    
    def get_shipment_status(self, order_id: str) -> Dict[str, Any]:
        return self.shipment_port.get_shipment_status(order_id)
    
    def cancel_shipment(self, order_id: str) -> Dict[str, Any]:
        return self.shipment_port.cancel_shipment(order_id)
    
    def tracking_shipment(self, tracking_number: str) -> Dict[str, Any]:
        return self.shipment_port.tracking_shipment(tracking_number)
