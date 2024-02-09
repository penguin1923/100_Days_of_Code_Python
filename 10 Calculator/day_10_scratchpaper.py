first =""
last =""

def format_name(f_name,l_name):
    first = f_name.title()
    last = l_name.title()
    return first,last

format_name("DOn","CoCo")
print(f"Hello {first} {last}!")
