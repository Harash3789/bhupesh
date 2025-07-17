# # # print("heello world")
# # # a ="hello" 
# # # num = 10
# # # # @ = 4
# # # # 2=2
# # # Age = 22
# # # age =23 
# # # print(Age)
# # # print(age)


# # # name = "Ritik kumar "
# # # print(name)
# # # print("my name is",name)
# # # print("name dtypes:-",type(name))
# # #  print("len of name:-",len{name})
# # # #    indexing
# # # # print(name[0])
# # # print(name[2])
# # # print(name[len(name)-1])
# # # slicing in python
# # # name = "ritik"
# # # print (name[0:4])


# # # home work

# # #operation 
# # name = "ritik"
# # last = " umawat"
# # # upper case =name.upper()upper function ka used upper case ke liye kerte hai 
# # # print(upper _case
# # )
# # # lower_last_name()
# # # print(lower_last_name)

# # # print (name.count("r"))
# # # print(name.title())
# # # print(name.capitalize())
# # print(name+last)


# # list =
# lst = [1,2,3,4,5,6,7] 
# # array or list >>>>>>>
# # mutable
# # duplicate value 
# # herto 
# # order 
# # array
# # array>>>>>> lat = [1,2,3,4,5,6]
# # array
# print("my first list:-",lst)
# print("len of list:-",len(lst))
# print ("type of list:-",type(lst))
# # print(list[o:5])
# # lst =[1,2,3,4,5,6,7, "rohit", 2,3]
# # lst.append(100)
# # print(lst)
# # lst.insert(0,1000)
# # print(lst)
# # copy_lst = lst.copy()
# # print(lst)
# # lst.remove(2.3)
# # print(lst)
# # lst.sort()
# lst =[1,2,3,4,5,6,7, "rohit", 2,3] ##>>>>>>>>> list

# print(lst.count(2))
# print(lst)


# >>>>>>>>>>>>>>>>>>>>tuple<<<<<<<<<<<<<<<<
# tpl = (1,2,3,5,585,5, "ritik" , 2.3)
# print("my first tuple:-", tpl)
# print("len of tuple:-",len(tpl))
# print ("type of tuple:-",type(tpl))
 
# a=1,2,58,5,58,5,5,85,2
# print(a)
# print(type(a))
# print(len(a))


# a,b,c=(1,2,3)
# print(a)
# print(b)
# print(c)
# a , b , c = 1,2,3
# print(a)
# print(b)
# print(c)



# tpl =91,2,58,2,8,2,8
# print("max of tuple =",)



# # >>>>>>>>>>>>>dict>>>>>>>
# my_dict ={
#     "name":"rohit",#######name, class , roll no. and address
#     "class": "2nd year",
#     "roll number":"23RU311038",
#     "address":"jaipur"

# }

# # print("my first dict:-",my dict)
# # print(len of dict:-,len(my dict))
# print("type of dict:-",type(my dict))
# print(my dict['name'])
# print(my dict['class'])
# print(my_dict)[roll number]

# access element 6




# lst = [1,2,3,4,[6],7]
# print("full lst:-",lst)
# nested =lst[4]
# print("nested lst:-",nested)
# six = nested[0]



# print("access element:-", six)



# print( my_dict.key())
# print( my_dict.value())
# print( my_dict.item())


# copy_dict =my_dict.copy()
# print(copy_dict)

#my_dict.clear()
# print(my_dict)


#  print(a*b)
# print(type(a))


# # type casting
# lst = [1,2,6,8,5,58]
# print("type is my list:-",lst)
# print("type of list:-",type(lst))
# tpl = tuple(lst)
# print("this os my tuple:-",tpl)
# print("type of tpl")



# my_set ={1,2,3,5,41,6,1,5, "jai"}
# print("this is my first set :-",my_set)
# print("lenof my set:-",len(my_set))
# print("type of set:-",type(my set))


# task>>>>
# my_set.union()
# my_set.intersection()
# my_set.difference()
# my_set




# student_scores = {"Alice": 95, "Bob": 88, "Charlie": 72}
# score_alice = student_scores.get("Alice")
# print(f"Alice's score: {score_alice}")




# student_scores = {"Alice": 95, "Bob": 88, "Charlie": 72}
# score_dave = student_scores.get("Dave")
# print(f"Dave's score: {score_dave}") # Output will be None



# student_scores = {"Alice": 95, "Bob": 88, "Charlie": 72}
# score_eve = student_scores.get("Eve", 0)
# print(f"Eve's score: {score_eve}") # Output will be 0


# config = {"debug_mode": True, "port": 8080}
# is_logging_enabled = config.get("enable_logging", False)
# print(f"Logging enabled: {is_logging_enabled}")


data = {
        "user_info": {
            "name": "harash",
            "contact": {"email": "jai@example.com"}
        }
    }
user_email = data.get("user_info", {}).get("contact", {}).get("email")
print(f"User email: {user_email}")
