from django.test import TestCase
from .models import CustomUser, Booking

class CustomUserTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = CustomUser.objects.create_user(
            email="test@example.com",
            password="password123",
            first_name="John",
            last_name="Doe",
            phone_number="1234567890",
        )

    def test_user_creation(self):
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.phone_number, "1234567890")
        self.assertFalse(self.user.is_verified)

    def test_get_full_name(self):
        full_name = self.user.get_full_name()
        self.assertEqual(full_name, "John Doe")

    def test_get_coordinates(self):
        # Test when coordinates are not set
        coordinates = self.user.get_coordinates()
        self.assertIsNone(coordinates)

        # Set coordinates and test again
        self.user.address = "123 Main St, City"
        self.user.set_coordinates()
        coordinates = self.user.get_coordinates()
        self.assertIsNotNone(coordinates)

    def test_set_minutes_away(self):
        # Test when pickup coordinates are not provided
        result = self.user.set_minutes_away("123.456,789.012", save=False)
        self.assertIsNone(result)

        # Set coordinates and test again
        self.user.address = "456 Elm St, Town"
        self.user.set_coordinates()
        result = self.user.set_minutes_away("123.456,789.012", save=False)
        self.assertIsNotNone(result)

    def test_set_minutes_away_save(self):
        # Set coordinates and test again, saving the result
        self.user.address = "789 Oak St, Village"
        self.user.set_coordinates()
        result = self.user.set_minutes_away("123.456,789.012", save=True)
        self.assertIsNotNone(result)
        self.assertIsNotNone(self.user.minutes_away)

    def test_str_representation(self):
        self.assertEqual(str(self.user), "John")

    def tearDown(self):
        # Clean up after each test
        self.user.delete()



class BookingTestCase(TestCase):
    def setUp(self):
        # Create a test booking
        # 6955 Mission Gorge Rd San Diego California
        # Latitude	32.79943 # Longitude	-117.091776
        
        # 700 Main St Louisville Colorado
        # Latitude	39.97695, Longitude	-105.131812
        
        
        self.booking = Booking.objects.create(
            pickup_location="6955 Mission Gorge Rd San Diego California",
            dropoff_location="700 Main St Louisville Colorado",
            email="test@example.com",
            tracking_id="ABC123",
            is_fulfilled=False,
            selected_item="3-5",
            vehicle_type="Cargo Van",
            service_type="LOAD",
            rate_type="HR",
            handle_loading="2",
            note="Test note",
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.pickup_location, "6955 Mission Gorge Rd San Diego California")
        self.assertEqual(self.booking.dropoff_location, "700 Main St Louisville Colorado")
        # self.assertEqual(self.booking.pickup_latitude, "123.456")
        # self.assertEqual(self.booking.pickup_longitude, "789.012")
        # self.assertEqual(self.booking.dropoff_latitude, "456.789")
        # self.assertEqual(self.booking.dropoff_longitude, "012.345")
        self.assertEqual(self.booking.email, "test@example.com")
        self.assertEqual(self.booking.selected_item, "3-5")
        self.assertEqual(self.booking.vehicle_type, "Cargo Van")
        self.assertEqual(self.booking.service_type, "LOAD")
        self.assertEqual(self.booking.rate_type, "HR")
        self.assertEqual(self.booking.handle_loading, "2")
        self.assertEqual(self.booking.note, "Test note")

    def test_coordinates_methods(self):
        # Test setting coordinates
        self.booking.set_coordinates()
        self.assertIsNotNone(self.booking.pickup_latitude)
        self.assertIsNotNone(self.booking.pickup_longitude)
        self.assertIsNotNone(self.booking.dropoff_latitude)
        self.assertIsNotNone(self.booking.dropoff_longitude)

        # Test getting coordinates
        pickup, dropoff = self.booking.get_coordinates()
        self.assertEqual(pickup, "123.456,789.012")
        self.assertEqual(dropoff, "456.789,012.345")

    def test_set_driving_data(self):
        # Test setting driving data
        self.booking.set_driving_data("Origin", "Destination")
        self.assertEqual(self.booking.estimated_duration, 60)
        self.assertEqual(self.booking.total_distance, 100)

    def test_string_representation(self):
        string_representation = str(self.booking)
        self.assertEqual(string_representation, "Booking - ABC123")

    def tearDown(self):
        # Clean up after each test
        self.booking.delete()
