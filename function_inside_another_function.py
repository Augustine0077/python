# # #punction inside another function

# # def process_student():
# #     def calculate_grade(mark):
# #         if mark >= 90:
# #             return "A"
# #         elif mark >= 75:
# #             return "B"
# #         else:
# #             return "C"
    
# #     return calculate_grade(82)

# # print(process_student())  

# def studyes(fun):
#     def kollamo():
#         print("studies ekke engane ponu")
#         fun()
#     return kollamo

# def sugamano(fun):
#     def wrap():
#         print("Sugam ano ")
#         fun()
#         print("Enthekke und")
#         fun()
#     return wrap

# @sugamano
# @studyes
# def greet():
#     print("Augustine")

# greet()



def first_decorator(func):
    def wrapper():
        print("This is the first decorator")
        func()
        func()
    return wrapper


def second_decorator(func):
    def wrapper():
        print("this is second decorator")
        func()
        func()
    return wrapper
@first_decorator
@second_decorator
def greet():
    print("hello augustine")
greet()