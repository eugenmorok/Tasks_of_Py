file = open("products.txt", encoding = "utf-8")
first_list = file.readlines()
first_list = sorted(first_list)
first_list = "".join(first_list)
print(first_list)
new_file = open("products.txt", "w", encoding = "utf-8")
new_file.write(first_list)
new_file.close()
file.close()