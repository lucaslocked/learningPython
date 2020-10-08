# def outer_function(msg):
#     message = msg

#     def inner_function():
#         print(message)
#     return inner_function()

# hi_func = outer_function('hi')
# bye_func = outer_function('bye')

def decorator_function(message):
    def wrapper_function():
        return message
    return wrapper_function

def display():
    print('The Display Function Ran')

decorated_display = decorator_function(display)

decorated_display()