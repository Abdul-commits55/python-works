#                     #Dictt .keys
# student={
#     "name":"Abu Bakar",
#     "Subject":{
#     "phy":91,
#     "maths":99,
#     "comp":100,
#     }
# }
# print(len(student))
# print(list(student.keys()))

                   # Dict.Values
# student={
#     "name":"Abu Bakar",
#     "Subject":{
#     "phy":91,
#     "maths":99,
#     "comp":100,
#     }
# }
# print(student.values())
                               
                               
                   # Dict.Iteam
# student={
#     "name":"Abu Bakar",
#     "Subject":{
#     "phy":91,
#     "maths":99,
#     "comp":100,
#     }
# }
# print(student.items())
                               
                     # Dict.IGet
student={
    "name":"Abu Bakar",
    "Subject":{
    "phy":91,
    "maths":99,
    "comp":100,
    }
}
# print(student["name2"])
print(student.get("name"))                  

                        #dict.update
student={
    "name":"Abu Bakar",
    "Subject":{
    "phy":91,
    "maths":99,
    "comp":100,
    }
}
student.update({"city":"Haripur"})
print(student)