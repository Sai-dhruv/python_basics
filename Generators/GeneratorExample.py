import random
import time

names =['sai','krishna','Niharika','Dhruv','sarath']
subject = ['Java','python', 'snowflake','spring boot']

def listexample(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id' : i,
                    'name' : random.choice(names),
                    'subject' : random.choice(subject)
        }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id' : i,
                    'name' : random.choice(names),
                    'subject' : random.choice(subject)
        }
        yield person

'''t1 = time.localtime().tm_sec
data = listexample(100000000000000)
t2 = time.localtime().tm_sec
print("Time difference :", (t2-t1))
'''

t1 = time.localtime().tm_sec
data = people_generator(1000000)
t2 = time.localtime().tm_sec
print("Time difference :", (t2-t1))
