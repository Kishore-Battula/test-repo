import json

grades_dict={
    'gradebook':
        [
            {'student_id':1,'name':'Red','grade':'A'},
            {'student_id':2,'name':"Yellow",'grade':'A'},
            {'student_id':3,'name':'White','grade':'C'}
        ]
}

with open('/Users/kishorebattula/Desktop/Kishore/grades_jason.txt','a') as records:
       json.dump(grades_dict,records)
       print('Grades.txt file was succesfully created.')

with open('/Users/kishorebattula/Desktop/Kishore/accounts_jason.txt','r') as records:
       print(json.dumps(json.load(records),indent=4))



