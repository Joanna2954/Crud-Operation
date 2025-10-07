from django.db import models

# Create your models here.

# * **Employee Name** â€“ cannot be blank 
# * **Age** â€“ must be a positive number 
# * **Email Address** â€“ should be unique (`unique=True`)
# * **Date of Joining** â€“ default value should be the current date (`default=date.today`)



class Employee(models.Model):
    name=models.CharField(max_length=30) 
    age=models.PositiveIntegerField()
    email=models.EmailField(unique=True)   
    date_of_joining=models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.name}--{self.email}"
        




# Create a table for products with the following details:

# * **Product Name** â€“ cannot be blank 
# * **Brand Name** â€“ optional 
# * **Price** â€“ must be a positive value 
# * **Manufacturing Date** â€“ store as a date field 


class Product(models.Model):
    Product_name=models.CharField(max_length=30)
    Brand_name=models.CharField(null=True)
    price=models.PositiveIntegerField()
    date_of_joining=models.DateField()

# Create a table for books with the following details: 

# * **Book Title** â€“ cannot be blank 
# * **Author Name** â€“ cannot be blank 
# * **Genre** â€“ optional 
# * **Published Year** â€“ store as an integer field 


class Books(models.Model):

    Book_Title=models.CharField(max_length=30)
    Author_name=models.CharField(max_length=30)
    Genre=models.CharField(null=True)
    Published_Year=models.IntegerField()

    def __str__(self):
        return f"{self.Book_Title}"


# Task 4 â€“ Movie Table**

# Create a table for movies with the following details:

# * **Movie Title** â€“ cannot be blank 
# * **Director Name** â€“ cannot be blank 
# * **Release Date** â€“ store as a date field 
# * **Language** â€“ default value should be `"English"` (`default="English"`)




class Movies(models.Model):

    Movie_Title=models.CharField(max_length=30,blank=False, null=False)
    Director=models.CharField(max_length=30,blank=False, null=False)
    Release=models.DateField()
    Language=models.CharField(default='English')







# Task 5 â€“ Student Table**

# Create a table for students with the following details:

# * **Student Name** â€“ cannot be blank 
# * **Age** â€“ must be a positive number 
# * **Email Address** â€“ should be unique 
# * **Date of Birth** â€“ store as a date field 



class Students(models.Model):

    student_name=models.CharField( max_length=30,blank=False, null=False)
    Age=models.PositiveIntegerField()
    Email=models.EmailField(unique=True)
    Date_of_Birth=models.DateField()
    Grade = models.CharField(max_length=2,blank=True,null=True)  
    Phone = models.CharField(max_length=15,blank=True,null=True)
    City = models.CharField(max_length=50,blank=True,null=True)
    admission_date = models.DateField(blank=True,null=True)
    is_active = models.BooleanField(default=True,blank=True,null=True)
   




class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)




class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    stock_quantity = models.IntegerField(null=True)


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author_name = models.CharField(max_length=50)
    published = models.BooleanField(default=False)


class Comment(models.Model):
    commenter_name = models.CharField(max_length=50)
    comment_text = models.TextField()
    blog = models.CharField()


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=50)
    duration_in_weeks = models.IntegerField()
    fee = models.FloatField()


class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=50)


#relationships: 
#one-to-one field
#one- to - many field => foriegnkey
#many -to -many fields


class Category(models.Model):
    name = models.CharField(max_length=50)
    des = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class product_model(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    cat_name = models.ForeignKey(Category,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    #models.CASCADE => if category gets deleted products also get deleted
    #models.SET_DEFAULT => we should give one default while declaration
    #SET_NULL => It will assign null
    #PROTECT => it will raise an error
    #DO_NOTHING => It will do nothing we should change manually




class courseModule(models.Model):
    name = models.CharField(max_length=50)
    Duration  = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class student_name(models.Model):
    name = models.CharField(max_length=50)
    Age=models.PositiveIntegerField()
    Email=models.EmailField(unique=True)
    course_name = models.ForeignKey(courseModule,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
