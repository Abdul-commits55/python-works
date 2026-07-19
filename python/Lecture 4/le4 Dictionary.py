# info ={
#     "key" : "value",
#     "name":"pana college",
#     "learning":"coding",
#     "age":356,
#     "subject":("diret","set",),
#     "topic":["pyhton","c","java","html","css"],
#     "is_adult":True,
# }
# info["name"]="abdulmohiz"
# print(type(info))
# info["name"]="abdulmohiz"
# print(info)

                    #nested dictionary
student={
    "name":"Abu Bakar",
    "Subject":{
    "phy":91,
    "maths":99,
    "comp":100,
    }
}
print(student)
print(student["Subject"])
print(student["Subject"]["comp"])