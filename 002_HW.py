#====================================================== if ოპერატპრი  #==============================================================================================
# x = 60
# y = 50

# if x > y :
#     print ('x>y')
#     print ('line 6')
# else: 
#     print ('x<y')
#     print ('line 9')

#======================================================
# name = 'Python'
# if name == 'C#':
#     print ('Hello C#')
# elif name == 'JavaScript':
#     print ('Hellow JS')
# elif name == 'Python':
#     print ('Hellow Python')
# elif name == 'C++':
#     print ('Hellow C++')
# else:
#     print ('ar vici romelia swori')

#======================================================
# name = 'Python'  # ასე ჯობია არ ჩაიწეროს, რადგან შესაძლოა იყოს ერორები 
# if name == 'C#':
#     print ('Hello C#')
# if name == 'JavaScript':
#     print ('Hellow JS')
# if name == 'Python':
#     print ('Hellow Python')
# if name == 'C++':
#     print ('Hellow C++')
# else:
#     print ('ar vici romelia swori')

#======================================================
# a = 25   # დავადგინოთ მცემული რიცხვი კენტია თუ ლუწი. 
# if a % 2 == 0:
#     print ('lutsia')
# else:
#     print ('kentia')

#======================================================
# import random    # ბბლიოთეკის დაიმპორტება 
# a = 15   # a-უნდა იყოფოდეს 5ზე და 3ზე b-უნდა იყოფოდეს 3ზე. გამოვიტანოთ შდეგი  
# b = 9  # random.randrange(1, 100)
# if  a % 3 == 0 and a % 5 == 0 : 
#     print (a, 'ikopa 3ze da 5ze')
# else: print (a, 'ar ikopa ertdroulad 3ze da 5ze')
# if  b % 3 == 0: 
#     print (b, 'ikofa 3ze')
# else: print(b, 'ar ikopa 3ze')

#======================================================
# name = 'python'
# if name =='c#':
#     pass # pass - ჩაშენებული  ფუნქციაა. პირობის გამოტოვება, გადახტომა, გამოიყენება თუ არ გავაქვს პირობა 
# elif name =='python':
#     print ('python')

#======================================================დაბადების წლით და მიმდინარე წლით დავადგინოთ გვაქვს თუ არა მართვის მოწმობის აღების უფლება
# b_year = int (input ('gtkhovt sheikvanet dabadebis tseli ')  )
# c_year = int(input ('gtkhovt sheikvanet mindianre tseli '))
# if c_year - b_year >= 18:
#     print ('gaqvt ufleba')
# else:
#     print ('ar gakvt ufleba')

#====================================================== დაადგინეთ რომელ კატეგორიაში მოხვდა თქვენი ქულა 
# y_point = int (input('gtkovt sheikvanet tkveni qula -  '))
# a = '90 dan 100mde'
# b = '80 dan 90mde'
# c = '70 dan 8mde'
# d = '60ze dabla'
# if 100 > y_point >= 90:
#     print ('tqven miiget A kaegoria',  a , 'kategoria')
# elif 90 > y_point >= 80:
#     print ('tqven miiget B kaegoria',  b , 'kategoria')
# elif 80 > y_point >= 70:
#     print ('tqven miiget C kaegoria',  b , 'kategoria')
# else:
#     print ('tqven miiget D kaegoria',  d , 'kategoria')

#====================================================== ასე ჯობდა ზედა დავალების შესრულება:
# y_point = int (input('gtkovt sheikvanet tkveni qula -  '))
# a = '90 dan 100mde'
# b = '80 dan 90mde'
# c = '70 dan 8mde'
# d = '60ze dabla'
# if 100 > y_point and y_point >= 90:
#     print ('tqven miiget A kaegoria',  a, 'reinji')
# elif 90 > y_point and y_point >= 80:
#     print ('tqven miiget B kaegoria',  b, 'reinji' )
# elif 80 > y_point and  y_point >= 70:
#     print ('tqven miiget C kaegoria',  b, 'reinji')
# else:
#     print ('tqven miiget D kaegoria',  d, 'reinji')



#====================================================== Python Try Except -  https://www.w3schools.com/python/python_try_except.asp #==============================================================================================

# The "try" block lets you test a block of code for errors.
# The "except" block lets you handle the error.
# The "else" block lets you execute code when there is no error.
# The "finally" block lets you execute code, regardless of the result of the try- and except blocks.
#======================================================

# try: 
#     a = int (input('number - '))
#     x = 1.0/a
#     print (x)
# except:    # თუ არ სრყლდება try, შესრულდება exceptგანპნაკლისი, ერთდრულად შეგვიძლაი გვქონდეს რამდენიმე 
#     print ('ver shesruldeba')
# finally: # იბეჭდება ბოლოში, ნებიმიერ შემთხვევაში. არაა სავალდებულო სტრიქონი
#     c = a + 5
#     print (c, 'saboloo bloks daemata 5')

#======================================================
# try: 
#     print (x)
# except NameError: # exception errors (არის ბევრი ერორი ასეთი ტიპის და უნდა მოვძებნო )
#     print ('ar aris agtserili')


#====================================================== Whihe ლუპი  #==============================================================================================

# i = 1
# while i < 6:
#     print (i)
#     i = i + 1

#======================================================
# i = 1
# while i < 6:
#     print(i)
#     i += 1

#======================================================
# i = 1
# while i < 6:
#     print (i)
#     i = i + 1
# else:
#     print ('bechdva dasrulda,  i gautolda 6ss')

#======================================================
# i = 1  # break - ასრულებს მითთებულ ნიშნულზე while-ის მუშაობას 
# while i < 6:
#     print (i)
#     i = i + 1
#     if i == 5:
#         break

#====================================================== 
# i = 1
# while i < 6:
#     print (i)
#     i = i + 1
#     if i == 10:
#         continue  # ვერ გავიგე არსი <???? @@@@@@@@@@>

#======================================================
# i = 0  # დავბეჭდოთ ლუწი რიცხვები 0დან 20მდე 'while' ლუპის გამოყენებით
# while i < 40:
#     i = i +1
#     if i % 2 == 0:
#         print (i)

#======================================================
# i = 1  # არ მუშაობს  <?????????????????? @@@@@@@@@> 
# while i < 6:
#     pass
# else: 
#     print ('tsikli ar dawkebula, radgan piroba aklia')


#====================================================== for ლუპი  #==============================================================================================

# for i in 'Georgia':
#     print(i)

#======================================================
# for i in range (100): # პირველი პარამეტრი დეფოლტად იგულისხმება 1, როცა არაა მითთებული
#     print(i)

#======================================================
# for i in range (100, 600):
#     print(i)

#======================================================
# for i in range (100, 600, 20):  # მესამე არის ბოჯი
#     print(i)

#======================================================
# for x in range (10):
#     if x == 10:
#         break 
#     print (x)
# else:
#     print('dasasruli')

#======================================================   დავთვალოთ ყველა რიცხვის ჯამი 0დან 120მდე 'for' ლუპით
# a = 0
# b = 120
# for i in range (b + 1): 
#     a = a + i 
# print(a)

#======================================================  12345 უნდა შევაბრუნოთ ასე:
# 54321
# 4321
# 321
# 21
# 1
# for i in range (5, 0, -1):
#     for j in range (i, 0, -1):
#         print (j, end = '')
#     print ()

#====================================================== დავბეჭდოთ ლუწი რიცხვები 0დან 20მდე 'for' ლუპის გამოყენებით 
# for i in range (20):
#     if i % 2 == 0:
#         print (i)

#====================================================== დავთვალოთ ყველა რიცხვის ჯამი 0დან 120მდე 'while' ლუპით
# sum = 0
# i = 1
# while i <= 120:
#     sum += i    
#     i += 1
# print(sum)

#====================================================== ჩამოვწეროთ კონტი რიცხვები მოცემულ რეინჯში, 
# minimum = int(input(" Please Enter the Minimum Value : "))
# maximum = int(input(" Please Enter the Maximum Value : "))
# for number in range(minimum, maximum+1):
#     if(number % 2 != 0):
#         print(number)
    