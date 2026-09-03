#! JSON :->
#? JavaScript Object Notation.  

#! JSON in Python
#* Python has a built-in package called json, which can be used to work with JSON data.

import json

#? Convert from JSON to Python:---->>
#* If you have a JSON string, you can parse it by using the json.loads() method. 
# example:-
json_data = '{"name": "Aanshi", "age": 30, "city": "New York"}'
print(json_data)
print(type(json_data))

py_data = json.loads(json_data) # convert into python data
print(py_data)
print(type(py_data))
print(py_data['name'])

#? Convert from Python to JSON:----->>
#* If you have a Python object, you can convert it into a JSON string by using the json.dumps() method. 
# example:-
py_data = {
    "name": "Mohan Kumar",
    "age": 35,
    "city": "New Delhi" 
}
print(py_data)
print(type(py_data))

json_data = json.dumps(py_data) # convert into json data
print(json_data)
print(type(json_data))
import data 
data.info("Yash Gupta", 25, "yashgupta@gmail.com")
