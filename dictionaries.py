capital = {"usa":"washington D.C.",
           "Russia":"Moscow",
           "India":"New Delhi"}
capital.update({"Germany":"Berlin"})
keys = capital.keys()
print(keys)
for key in keys:
    print(key)
values = capital.values()
for value in values:
    print(value)
for key,value in capital.items():
    print (f"{key}:{value}")