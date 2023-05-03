import os
import sys
import unittest
import json
from app import create_app

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = create_app()

class TestPaymentsController(unittest.TestCase):
    def setUp(self):
        self.cliente = app.test_client()
        self.transaction_data = {
            "user_id": 1,
            "card_id": 2,
            "date_hour": '2023-05-03 12:20:30',
            "mount": 50.0,
            "state": 'PENDING'
        }
    
    def test_create_payment(self):
        response = self.cliente.post('/payments/create',data=json.dumps(self.transaction_data),content_type='application/json')
        self.assertEqual(response.status_code,200)
        transaction_id = json.loads(response.get_data())['id']
        self.assertIsNotNone(transaction_id)