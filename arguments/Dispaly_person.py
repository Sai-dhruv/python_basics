def display_person_1(*args):
    for i in args:
        print(i)

def display_person(**kwargs):
    for k,v in kwargs.items():
        print(k ," and the value is ",v)



display_person(name="saikrishna",age=33)  # Type Error      
display_person_1(10,29,23,23,12,3,312,32,32,12,23)
