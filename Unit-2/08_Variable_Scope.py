
# Demonstrate local, global, and nonlocal variables

global_var = "I am a global variable"

def show_local():
    local_var = "I am a local variable"
    print("Local:", local_var)

def show_global():
    print("Global:", global_var)

def show_nonlocal():
    message = "Original message"

    def inner():
        nonlocal message
        message = "Updated by inner function"

    inner()
    print("Nonlocal:", message)

show_local()
show_global()
show_nonlocal()
