from rest_framework import serializers
from passenger.models import Payment
from authentication.models import Passenger,CustomUser
from authentication.serializers import PassengerSerializer
from booking.models import Booking
from booking.serializers import BookingSerializer

class PaymentSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer(read_only=True)
    booking = BookingSerializer(read_only=True)
    

    class Meta:
        model = Payment
        fields = '__all__'
        extra_kwargs = {
            'amount_paid': {'required': False},
            'transaction_id': {'required': False},
            
        }

    def validate(self, data):
        booking_id = self.context.get('booking_id')

        try:
            booking = Booking.objects.get(booking_id=booking_id)
        except Booking.DoesNotExist:
            raise serializers.ValidationError({"booking_id": "Invalid booking ID."})

        # Prevent updates if payment is already successful
        if self.instance and self.instance.is_successful:
            raise serializers.ValidationError("This payment has already been completed and cannot be updated.")

        # Check payment method validity
        if data['payment_method'] not in dict(Payment.PAYMENT_METHOD_CHOICES).keys():
            raise serializers.ValidationError("Invalid payment method.")

        # Check if amount_paid is provided and if it matches booking price
        if 'amount_paid' in data:
            if data['amount_paid'] != booking.price:
                raise serializers.ValidationError("Amount paid must equal the booking price.")
        else:
            # Automatically set the amount_paid to the booking price
            data['amount_paid'] = booking.price

        return data

    def create(self, validated_data):
        booking_id = self.context.get('booking_id')
        try:
            booking = Booking.objects.get(booking_id=booking_id)
        except Booking.DoesNotExist:
            raise serializers.ValidationError({"booking_id": "Invalid booking ID."})

        # Check if there's already a successful payment for this booking
        existing_payment = Payment.objects.filter(booking=booking, is_successful=True).first()
        if existing_payment:
            raise serializers.ValidationError("A successful payment already exists for this booking. Cannot create another payment.")

        username = self.context['username']
        user = CustomUser.objects.get(username=username)
        passenger = Passenger.objects.get(user=user)
        validated_data['passenger'] = passenger
        validated_data['booking'] = booking

        # Automatically set the amount_paid to the booking price if not provided
        if 'amount_paid' not in validated_data:
            validated_data['amount_paid'] = booking.price

        # Create payment and mark it as successful
        payment = Payment.objects.create(**validated_data)
        payment.is_successful = True
        payment.save()
        if payment.is_successful:
            booking.is_paid = True
            booking.save()
            
        return payment

    def update(self, instance, validated_data):
        if instance.is_successful:
            raise serializers.ValidationError("This payment has already been completed and cannot be updated.")
        
        return super().update(instance, validated_data)

    def delete(self, instance):
        if instance.is_successful:
            raise serializers.ValidationError("This payment has already been completed and cannot be deleted.")
        
        instance.delete()
    
    
