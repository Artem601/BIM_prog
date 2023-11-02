numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

cumma=sum(numbers[:4])
summa=sum(numbers[5:])
s=summa+cumma
count=len(numbers)
rez=s/count
numbers[4]=rez
print("Измененный список:", numbers)