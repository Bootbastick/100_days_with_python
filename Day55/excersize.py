# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*kwargs):
        name_of_the_function = function.__name__
        output = function(kwargs[0])
        arguments = [kwargs]
        print(f"Name of the function is: {name_of_the_function}")
        print(f"All the arguments are in this list: {arguments}")
        print(f"The output is: {output}")

    return wrapper


# Use the decorator 👇
@logging_decorator
def hello_user(username):
    return f"Hello {username}!"


hello_user("John")
