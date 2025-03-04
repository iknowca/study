# Sort

`sorted`는 정렬 후 새로운 객체를 반환하고, `sort`는 정렬 후 객체를 직접 변경(inplace)한다.
`key`옵션능 사용하여 기준을 정할 수 있으며, `reverse` 옵션으로 올림차수 혹은 내림차순을 정할 수 있다.
```python
f_list =["orrange", "apple", "banana"]

print("sorted: ", sorted(f_list))
print("sorted: ", sorted(f_list, reverse=True))
print("sorted: ", sorted(f_list, key=len))
print("sorted: ", sorted(f_list, key=lambda x: x[-1]))
print("sorted: ", sorted(f_list, key=lambda x: x[-1], reverse=True))

print(f_list)

print("sort: ", f_list.sort(), f_list)
print("sort: ", f_list.sort(reverse=True), f_list)
print("sort: ", f_list.sort(key=lambda x: x[-1], reverse=True), f_list)

print(f_list)

# sorted :  ['apple', 'lemon', 'mango', 'orange']
# sorted :  ['orange', 'mango', 'lemon', 'apple']
# sorted :  ['apple', 'mango', 'lemon', 'orange']
# sorted :  ['orange', 'apple', 'lemon', 'mango']
# sorted :  ['mango', 'lemon', 'orange', 'apple']
# ['orange', 'apple', 'mango', 'lemon']
# sort :  None , ['apple', 'lemon', 'mango', 'orange']
# sort :  None , ['orange', 'mango', 'lemon', 'apple']
# sort :  None , ['mango', 'lemon', 'orange', 'apple']
# ['mango', 'lemon', 'orange', 'apple']
```

