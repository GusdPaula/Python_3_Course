# Try, except and finally

try:
    print(1)

except:
    print(3)

else: # It will run when you don't get errors
    print(5)

finally: # This will always run, Id doesn't metter if you got an error or not
    print(2)

###########################

# raise - exeptions
print(123)
raise ValueError("Got an error")
print(456)

