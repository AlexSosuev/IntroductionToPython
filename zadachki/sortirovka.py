# Быстрая сортировка
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))

# Сортировка слиянием


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        rigth = nums[mid:]
        merge_sort(left)
        merge_sort(rigth)
        i = j = k = 0
        while i < len(left) and j < len(rigth):
            if left[i] < rigth[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = rigth[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(rigth):
            nums[k] = rigth[j]
            j += 1
            k += 1


list_1 = [1, 5, 6, 9, 8, 7, 2, 1, 55, 2, 4]
merge_sort(list_1)
print(list_1)
