
# my_dict = {
# "name": "Dimka",
# "utf_8": lambda d: d.decode("utf-8")
# }


# data = my_dict["utf_8"](b"Coding")

# print(type(data))


TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for  key, value in TEST_CASES.items():

  
    print(key ,"===", value)