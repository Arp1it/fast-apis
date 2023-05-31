def add(firstName: str | list[int, int, str] | None, lastName: str = None):
    if(firstName != None):
        firstName.capitalize()

    return firstName + " " + lastName

fname = None
lname = "Gates"

name = add(fname, lname)

print(name)