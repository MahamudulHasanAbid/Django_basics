from django.shortcuts import render
from .models import Std, Teacher
# Create your views here.

def home(request):
    #Will retrive all objects : all()

    # std_info = Std.objects.all()  
    # print("return:", std_info)       #Will show the QuerySet which we will get through objects.all()
    # print("\nSQL query: ", std_info.query)    # return how to write in sql query means how all data will be retrived.

    #Will retrive specific objects and show those data on the table : filter().
    
    # std_info = Std.objects.filter(city = 'Dhaka')
    # print("return: ", std_info)
    # print("\nSQL query: ", std_info.query)

    #Will omit specific objects and show the lefted data on the table : exclude().
    
    # std_info = Std.objects.exclude(pass_date = '2024-04-23')
    # print("return: ", std_info)
    # print("\nSQL query: ", std_info.query)

    #Will order the table according to ascending or descending or randomly: order_by() and reverse()
    
    # std_info = Std.objects.order_by('roll')
    # std_info = Std.objects.order_by('-marks')
    # std_info = Std.objects.order_by('city')
    # std_info = Std.objects.order_by('?') # will generate random order list
    # std_info = Std.objects.order_by('-pass_date')
    # std_info = Std.objects.order_by('roll').reverse()
    # std_info = Std.objects.order_by('roll').reverse()[2:]
    # print("return: ", std_info)
    # print("\nSQL query: ", std_info.query)

    # Will retrive all objects but return dictionary instead of QuerySet
    # std_info = Std.objects.values()
    # std_info = Std.objects.values('name', 'pass_date')
    # print("return: ", std_info)
    # print("\nSQL query: ", std_info.query)

    # Will retrive all objects but return tuples instead of QuerySet

    # std_info = Std.objects.values_list()
    # std_info = Std.objects.values_list(named= True)
    # std_info = Std.objects.values_list('id', 'name', named= True)
    # print("return: ", std_info)
    # print("\nSQL query: ", std_info.query)

    # return render(request, 'index.html', {'students':std_info})


# ###################### Second Table started##########################
    stdquery = Std.objects.values_list('id', 'name', 'city', named= True)
    teacherquery = Teacher.objects.values_list('id', 'name', 'city', named= True)
    std_info = teacherquery.union(stdquery, all=True)
    # same as intersection() but It will return the shared data which is in both table.
    print("return: ", std_info)
    print("\nSQL query: ", std_info.query)

# DO not return QuerySet examples(Let these line be in comment.).

    # >>> Std.objects.filter(pk=2)            
    # <QuerySet [<Std: Std object (2)>]>
    # >>> Std.objects.filter(pk=2).get()
    # <Std: Std object (2)>
 
    return render(request, 'index.html', {'students':std_info})