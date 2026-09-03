#! DATA TYPES :- 
# Python Data Types are used to define the type of a variable.
#? Basically, Data Type ek vo h tarika hai jisse pta kiya ja sakta hai ki variable me kis type ka data store hai, like as number, text, boolean etc.

"""
    There are different types of data types in python:
    1. Numeric Types - (int, float, complex)
    2. Text Types - (str)
    3. Sequence Types - (list, tuple)
    4. Set Types - (set)
    5. Mapping - (dict)
    6. Boolean Types - (bool)
"""

#? 1. Numeric Types 
#* (int) - "bina point/dot vale numbers, jo ki whole number hote hain unhe, integer kahte hai." 
i_num = 0
print(i_num)

#* (float) - "basically point vale numbers ko float kahte hain like as a percentage."
f_num = 56.8
print(f_num)

#* (complex) - "number ke sath-sath ek characters bhi define hona, complex variable kahalate hai."
c_num = 45 + 6j
print(c_num)

#? Text Types (str) :------------------
# basically, text ka mean hai multiple characters ko mila kar jo banta hai vah string kahalata hai like as: "Hello World!" - generally string "double" or 'single' quotes me likhi jati hai, yahan double or single quotes me koi bhi fark nahi hai. 
your_info = "i love python Prog. Language."
print(your_info)

data = "where are you going?"
print(data)

love = "I love Python Programming Language." 
print(love)

info = "Hi Yash!, Kaise ho- ghar par sab thik hain?"
print(info)

#? 3. Sequence - (list, tuple) :-------------------------
# basically, sequence data types multiple values ko ek single variable me sequentially store karte hain, jinme square brackets [] or parenthesis () use kiye jata hai. Or actual me inka use hi single variable me multiple values store karne ke liye hi kiya jata hai.

#* list ------- 'list [] square brackets ka use karke banti hai, jisme har element ko seperate rakhne ke liye comma ka use kiya jata hai like as: ['Mohan', 'Sohan']'
names = ["Mohan", "Sohan", "Anuj", "Gopal", "girdhari"]
print(names)
"""
    lenght - 'lenght ka matlab hota hai ki, list me kitni values store hain? jaise names ki lenght = 5
              lenght 1 se start hoti hai.
    index - 'python me list me jo bhi variable aap store karte ho unka koi address jarur hota hai, or usi address ko list ki language me index bol dete hai.
              index 0 se start hota hai.

    agar lenght se index nikalna ho to formula:
    index = lenght - 1
    list ----- ["Mohan", "Sohan", "Anuj", "Gopal", "Girdhari"]
    lenght ----    1        2        3       4          5      
    index -----    0        1        2       3          4         
"""

# ab list me se kisi ek element/value ko nikalne ke liye index ka use kiya jata hai, means iske har element ko ek ek index define hai, jaise pahle element ko 0, dusre ko 1, tisre ko 2, and etc. 
print(names[1])
print(names[4])
print(names[3])
print(names[2], names[0])

# NOTE--- comma operator ka use elements ko seperate rakhne ke liye kiya jata hai.
# NOTE--- basically - list data type, mutable data type hota hai- iska matlab hai ki aap list me changes kar sakte ho (mtlab values re-assign kar sakte ho).

# ab agar mujhe koi value re-assign karni hai to:
names[1] = "Ayushi"
print(names)

names[4] = "Ritika"
print(names)

# *tuple ------- 'tuple () parenthesis ka use karke banta hai, jo ki kaffi similar hota hai list se, like as: ('Gopal', 'Girdhari')'
cities = ('noida', 'grater noida', 'new delhi', 'delhi', 'old delhi')
print(cities[3])

# yahan par bhi tuple ki values/elements ko nikalne ke liye indexes ka use kiya jata hai, jaise list me diye gaye hain.

# NOTE--- basically - tuple ek immutable data type hai- matlab isme changes nahi kar sakte. jaise aap list ke elements ko update karte hain vaise tuple me nahi kar sakte.
# cities[2] = 'hathras' ❌
# print(cities) ❌

# TODO---- 'list' or 'tuple' ek sequancial data types hain, jinme index use hota hai- means har element ko ek index hota hai jiska use karke ham 'list' ya 'tuple' ko iterate kar sakte hai. LEKIN JO SET HOTA HAI VO NON-SEQUAL DATA TYPES HAI, JISME INDEX KUCH BHI KAAM NAHI KARTA- MATLAB SET KE ELEMENTS KA KOI BHI INDEX NAHI HOTA HAI.

#? 4. Set - (set) ---------- 
#* basically, set bhi ek 'list' or 'tuple' ki trah hi data type hai jo ki multiple values ko store karta hai lekin iska koi sequence nahi hota hai, jab bhi aap set ko print karoge to values aage-piche hokar dikhengi. 
# set - curly-bracktes {} ka use karke banta hai like as: {'ayushi', 'anupam'}
fruits = {'orange', 'mango', 'papaya', 'banana'}
print(fruits)

#? 5. Mapping - (dict.) ----------
#* basically, dict. ka use details/info ko sahi tarike se store karne ke liye kiya jata hai, jisme 'key' or 'value' ka pair banta hai or isi ko 'property' kahte hain.
""" syntax :-
        var_name = {
            key: value,
            key: value
        }

    example: -
        user = {
            'id': 1,
            'name': 'Mohan',
            'city': 'Hathras'
        }
"""
user = {
    'id': 1,
    "name": 'Ayushi Jain',
    'email':'jainayushi7653@gmail.com',
    'city': 'New Delhi',
    'phone': 8767569854
}
# dict ki properties ko access karna hai to:
print(user["name"])
print(user['email'])
print(user['phone'])

# NOTE --- dict ki properties ko access karne ke liye square bracktes ke under key ka naam likhne se value nikal aayegi.

#? 6. Boolean - (bool) ----------
#* basically, boolean ka matlab hi 'True' or 'False' hai. ye jyadatar conditions ka status batata hai.
bank_status = True
print(bank_status) 

phone_status = False
print(phone_status)

info_name = mukul = True
print(info_name)

age = 20
if age > 18:
    print("you are eligible for voting.")
else:
    print("you are not eligible for voting")


#! Yahan tak to sab thik hai, lekin agar mujhe nahi pata ki variable me kis type ki value store hai to main kaise pta karunga?
#* uske liye ke function hota hai jisme ham "type()" function kahte hain, jiska use sirf or sirf kisi bhi variable me stored data ka type btane ke liye kiya jata hai:

x = 90
print(type(x)) 
 
y = "Ayushi"
print(type(y))

l = True
print(type(l))

m = {'id': 1}
print(type(m))

names = ["Mohit", "nitin", "Mukul", "seema", "Anshul"]

for word in names:
    for l in word:
        print(l)