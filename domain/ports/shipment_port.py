from abc import ABC, abstractmethod
from typing import Any, Dict, List

class ShipmentPort(ABC):
    @abstractmethod
    def create_shipment(self, order_id: str, recipient_name: str, recipient_address: str) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    def get_shipment_status(self, order_id: str) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    def cancel_shipment(self, order_id: str) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    def tracking_shipment(self, tracking_number: str) -> Dict[str, Any]:
        pass
