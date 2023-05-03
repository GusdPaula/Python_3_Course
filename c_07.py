# try, except, elese amd finally

# Errors cannot be silencied, although they are explicity silencied

# The exeption should be explicity

try:
    a = 18
    b = 0[0]
    c = a / b

except ZeroDivisionError:
    print("Divided by zero")

except NameError:
    print("Some letter is not definied...")

except Exception as error:
    print("Unknown error!")
    print("MSG:", error)
    print("Name:", error.__class__.__name__)