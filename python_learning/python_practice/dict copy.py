from typing import Dict , union , optional
my_dict: dict[str , union[str,list[str],int]] = {"name":"mubarra", "age":"20","course":["python","nextjs"]}
print(my_dict)


dict1:dict[str , union[str , int ,optional[list[str]]]] = {"name":"mubarra" , "age":"20"}



my_dict["name"].upper()
my_dict["courses"].append("java")
my_dict.get("name").upper()

my_dict.clear()
my_dict.fromkeys(["mubarra","python"])
my_dict["roll_num"] = "bs34"
my_dict[1] = 34