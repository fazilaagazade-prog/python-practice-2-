full_name = input("Ad ve soyadinizi daxil edin: ")

parts = full_name.split()

result = ""
for word in parts:
    result += word[0].upper() + "."

print(result)