from django.shortcuts import render,HttpResponse

# Create your views here.


#class based view 


#function based view

from praisy.models import *
def getall_books(request):
    books = Books.objects.all()
    # book = Books.objects.get(id=2)
    # book.Author_name = "Kalki"
    # book.save() 
    # book.delete()
    b= Books.objects.create(Book_Title="Mahabarath",Author_name="Valmeegi",Genre="Old books",Published_Year=1965)
    # print(book)
    fil = Books.objects.filter(Author_name="Kambar")
    print(fil)
    for i in books:
        print(i.Author_name)
    print(books)
    return HttpResponse(books)
   

def getall_users(request):
     user=User.objects.create(name="joselin", email="jose@example.com")
     user= User.objects.create(name="freeda", email="freeda@example.com")
     user= User.objects.create(name="joanna", email="joanna@example.com")
     return HttpResponse(user)


def get_products(request):
    product=Product.objects.create(name="Laptop", price=50000, stock_quantity=5)
    product= Product.objects.create(name="IPhone", price=40000, stock_quantity=10)      #phone
    product=Product.objects.create(name="Headphones", price=4000, stock_quantity=30)
    product=Product.objects.create(name="Ipad", price=35000, stock_quantity=8)          #tablet
    product=Product.objects.create(name="charger", price=700, stock_quantity=15)  #keyboard
    return HttpResponse(product)


def get_students(request):
     student=Students.objects.create(name="David", age=20, grade=95)
     student=Students.objects.create(name="Eva", age=19, grade=88)
     student=Students.objects.create(name="Francis", age=21, grade=76)
     return HttpResponse(student)


def get_blogs(request):
      blog=Blog.objects.create(title="Day in My Life", content="Fun", author_name="Freeda")
      blog=Blog.objects.create(title="Get Ready With Me <3", content="Selfcare", author_name="JOselin")
      blog=Blog.objects.create(title="A Day In My Life As Developer", content="Depression at peak", author_name="Joanna")
      return HttpResponse(blog)

def increase_stock(request):
    product = Product.objects.get(name="Laptop")
    product.stock_quantity += 10
    product.save()
    return HttpResponse(" Stock increased")


def add_comments(request):
    blog = Blog.objects.get(title="Django Basics")
    Comment.objects.create(commenter_name="John", comment_text="Nice post!", blog=blog)
    Comment.objects.create(commenter_name="Mary", comment_text="Very helpful", blog=blog)
    return HttpResponse(" Comments added")


def list_comments(request):
    blog = Blog.objects.get(title="Django Basics")
    comments = blog.comments.all()
    return HttpResponse(comments)




# def posts_by_author(request):
#     result = Blog.objects.values("author_name").annotate(count=Count("id"))
#     return HttpResponse(result)


# def avg_product_price(request):
#     result = Product.objects.aggregate(avg_price=Avg("price"))
#     return HttpResponse(result)


# def authors_with_more_posts(request):
#     result = Blog.objects.values("author_name").annotate(count=Count("id")).filter(count__gt=2)
#     return HttpResponse(result)


# def total_stock(request):
#     result = Product.objects.aggregate(total=Sum("stock_quantity"))
#     return HttpResponse(result)



from praisy.serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from praisy.models import *

@api_view(['GET'])
def Customer_view(request):
    customers = Customer.objects.all()
    serializers = CustomerSerializer(customers,many=True)
    return Response({"success":"True","customers_data":serializers.data})


@api_view(['POST'])
def customer_post(request):
    if request.method=="POST":
        serializers = CustomerSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
        return Response({"msg":"saved","data":serializers.data})
    

from rest_framework.views import APIView

class CustomerAPIView(APIView):
    def get(self,request):
        customers = Customer.objects.all()
        serializers = CustomerSerializer(customers,many=True)
        return Response({"customers_data":serializers.data})
    def post(self,request):
        if request.method=="POST":
            serializers = CustomerSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
            return Response({"msg":"saved","data":serializers.data})
        
class Customer_Single(APIView):
    def get(self,request,cus_id):
        cus = Customer.objects.get(id=cus_id)
        serializers = CustomerSerializer(cus)
        return Response(serializers.data)
    
    def put(self, request,cus_id):
        cus = Customer.objects.get(id=cus_id)
        serializers = CustomerSerializer(data=request.data,instance = cus)
        if serializers.is_valid():
            serializers.save()
        return Response({"msg":"updated","data":serializers.data})
    def delete(self,request,cus_id):

        cus = Customer.objects.get(id=cus_id)
        cus.delete()
        return Response({"msg":"deleted"})






# class Students(models.Model):

#     student_name=models.CharField( max_length=30,blank=False, null=False)
#     Age=models.PositiveIntegerField()
#     Email=models.EmailField(unique=True)
#     Date_of_Birth=models.DateField()

class Student_det(APIView):
      def get(self,request):   
        studt=Students.objects.all()
        serialize=StudentSerializer(studt,many=True)
        return Response({'student_details':serialize.data})



      def post(self,request):
        if request.method=="POST":
            serializer =StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response({"Details":"saved","data":serializer.data})
class student_edit(APIView):
      def get(self,request,std_id):   
        studt=Students.objects.get(id=std_id)
        serialize=StudentSerializer(studt)
        return Response({'student_details':serialize.data})
      
      def put(self, request,std_id):
         std = Students.objects.get(id=std_id)
         serializers = StudentSerializer(data=request.data,instance = std)
         if serializers.is_valid():
            serializers.save()
         return Response({"msg":"updated","data":serializers.data})
      def delete(self,request,std_id):

          std = Students.objects.get(id=std_id)
          std.delete()
          return Response({"msg":"deleted"})



# ✅ **Student API – CRUD Task**

# **📌 Model Fields:**

# * `name` – CharField
# * `age` – IntegerField
# * `grade` – CharField (e.g., "A", "B", etc.)
# * `email` – EmailField (unique)
# * `phone` – CharField
# * `city` – CharField
# * `admission_date` – DateField
# * `is_active` – BooleanField
# ---

# ### ✅ **Tasks:**

# #### 🔹 1. **Model**

# * Create a `Student` model with the above fields.
# * Use proper field types and add any required validators (e.g., for phone).

# #### 🔹 2. **Serializer**

# * Create a `StudentSerializer` using `ModelSerializer`.

# #### 🔹 3. **CRUD API Views**
# I

# * `GET /students/` → List all students
# * `GET /students/<id>/` → Retrieve a specific student
# * `POST /students/` → Add a new student
# * `PUT /students/<id>/` or `PATCH /students/<id>/` → Update existing student
# * `DELETE /students/<id>/` → Delete a student



class category_det(APIView):
      def get(self,request):   
        cate=Category.objects.all()
        serialize=CathegorySerializer(cate,many=True)
        return Response({'category_details':serialize.data})
      



      def post(self,request):
        if request.method=="POST":
            serializer =CathegorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response({"Details":"saved","data":serializer.data})
        


class product_det(APIView):
      def get(self,request):   
        prot=product_model.objects.all()
        serialize=productmodelSerializer(prot,many=True)
        return Response({'product_details':serialize.data})
      



      def post(self,request):
        if request.method=="POST":
            serializer =productmodelSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response({"Details":"saved","data":serializer.data})

class product_get(APIView):
      def get(self,request,pro_id):   
        cat=product_model.objects.get(id=pro_id)
        serialize=productmodelSerializer(cat)
        return Response({'pro_details':serialize.data})        
      
#########################################################################

# class course_get(APIView):
#       def get(self,request,st_id):   
#         cats=product_model.objects.get(id=st_id)
#         serialize=productmodelSerializer(cats)
#         return Response({'pro_details':serialize.data})   

# class course_det(APIView):
#       def get(self,request):   
#         stud=Course.objects.all()
#         serialize=CourseSerializer(stud,many=True)
#         return Response({'cousre_details':serialize.data})
      



#       def post(self,request):
#         if request.method=="POST":
#             serializer =CourseSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#             return Response({"Details":"saved","data":serializer.data})
        


class stud_det(APIView):
      def get(self,request):   
        cos=student_name.objects.all()
        serialize=studentnameSerializer(cos,many=True)
        return Response({'student_details':serialize.data})
      



      def post(self,request):
        if request.method=="POST":
            serializer =studentnameSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response({"Details":"saved","data":serializer.data})

 
    


class course_edit(APIView):
      def get(self,request,st_id):   
        studt=student_name.objects.get(id=st_id)
        serialize=studentnameSerializer(studt)
        return Response({'student_details':serialize.data})
      
      def put(self, request,st_id):
         std = student_name.objects.get(id=st_id)
         serializers = studentnameSerializer(data=request.data,instance = std)
         if serializers.is_valid():
            serializers.save()
         return Response({"msg":"updated","data":serializers.data})
      def delete(self,request,st_id):

          std = student_name.objects.get(id=st_id)
          std.delete()
          return Response({"msg":"deleted"})