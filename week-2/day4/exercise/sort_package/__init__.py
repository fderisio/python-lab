from .bubble_sort import bubble_sort
from .selection_sort import selection_sort
from .insertion_sort import insertion_sort
from .quick_sort import quick_sort

list1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(list1)
print(list1)

list2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(list2)
print(list2)

list3 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(list3)
print(list3)

list4 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(list4)
print(list4)
