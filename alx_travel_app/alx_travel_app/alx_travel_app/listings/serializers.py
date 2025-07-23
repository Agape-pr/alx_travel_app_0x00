from rest_framework import serializers
from .models import Listing, Booking, Review
from django.conf import settings

class ListingSerializer(serializers.ModelSerializer):
    host = serializers.StringRelatedField(read_only=True)  # show host as string (e.g., email or __str__)
    
    class Meta:
        model = Listing
        fields = [
            'listing_id',
            'host',
            'title',
            'description',
            'address',
            'price_per_night',
            'is_available',
            'created_at',
        ]

class BookingSerializer(serializers.ModelSerializer):
    guest = serializers.StringRelatedField(read_only=True)
    listing = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Booking
        fields = [
            'booking_id',
            'guest',
            'listing',
            'check_in',
            'check_out',
            'total_price',
            'created_at',
        ]

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField(read_only=True)
    listing = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = [
            'review_id',
            'reviewer',
            'listing',
            'rating',
            'comment',
            'created_at',
        ]
