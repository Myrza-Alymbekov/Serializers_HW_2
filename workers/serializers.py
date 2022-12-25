from rest_framework import serializers

from .models import Position, Employee


class PositionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    department = serializers.CharField(max_length=50)

    def create(self, validated_data):
        position = Position.objects.create(
            name=validated_data['name'],
            department=validated_data['department'],
        )
        return position

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.department = validated_data['department']
        return instance


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    birth_date = serializers.DateField()
    position_id = serializers.IntegerField()
    salary = serializers.IntegerField()

    def create(self, validated_data):
        employee = Employee.objects.create(
            name=validated_data['name'],
            birth_date=validated_data['birth_date'],
            position_id=validated_data['position_id'],
            salary=validated_data['salary'],
        )
        return employee

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.birth_date = validated_data['birth_date']
        instance.position_id = validated_data['position_id']
        instance.salary = validated_data['salary']
        return instance

