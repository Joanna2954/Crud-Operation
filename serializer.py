from rest_framework import serializers
from praisy.models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"  #['id','name'], exclude => it will exclude which is mentioned there

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields="__all__"




class CathegorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= "__all__"



class productmodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_model
        fields= "__all__"   
        depth =1     


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = courseModule
        fields= "__all__"



class studentnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = student_name
        fields= "__all__"   
        depth =1    
