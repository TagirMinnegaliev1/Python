cat_count = 0
first_cat_line = 0
line_number = 1

while True:
    str = input()
    if str == "СТОП":
        break

    if "кот" in str:
        cat_count += 1
        if first_cat_line == 0:
            first_cat_line = line_number

    line_number += 1

print(cat_count, first_cat_line)