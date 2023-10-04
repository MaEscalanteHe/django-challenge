from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import Product


class ProductModelTestCase(TestCase):
    def setUp(self):
        Product.objects.create(
            name="Laptop",
            description="Powerful laptop",
            price=1000.00,
            quantity=10,
            category="Electronics",
        )

    def test_product_creation(self):
        product = Product.objects.get(name="Laptop")
        self.assertEqual(product.description, "Powerful laptop")
        self.assertEqual(product.category, "Electronics")


class ProductApiTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Product.objects.create(
            name="Laptop",
            description="Powerful laptop",
            price=1000.00,
            quantity=10,
            category="Electronics",
        )
        Product.objects.create(
            name="Shirt",
            description="White shirt",
            price=20.00,
            quantity=50,
            category="Clothing",
        )

    def test_list_products(self):
        response = self.client.get("/v1/products/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

    def test_filter_by_name(self):
        response = self.client.get("/v1/products/?name=Laptop")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["name"], "Laptop")

    def test_filter_by_category(self):
        response = self.client.get("/v1/products/?category=Clothing")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["name"], "Shirt")

    def test_filter_by_min_price(self):
        response = self.client.get("/v1/products/?min_price=50")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["name"], "Laptop")

    def test_filter_by_max_price(self):
        response = self.client.get("/v1/products/?max_price=50")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["name"], "Shirt")

    def test_multiple_queries(self):
        response = self.client.get(
            "/v1/products/?name=Laptop&category=Electronics&min_price=500"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["name"], "Laptop")

    def test_price_range(self):
        response = self.client.get("/v1/products/?min_price=10&max_price=50")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["name"], "Shirt")
