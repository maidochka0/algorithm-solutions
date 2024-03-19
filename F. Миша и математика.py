def get_odd_expression():
    def is_odd(num):
        return num % 2 == 1
    
    char_list = []
    odd_island_count = 0
    old = nums[0] - 1
    for i in nums:
        if is_odd(i) != is_odd(old):
            char_list.append('+')
            if is_odd(i):
                odd_island_count += 1
        else:
            char_list.append('x')
        old = i
    if not is_odd(odd_island_count):
        i = 0
        while not is_odd(nums[i]):
            i += 1
        if not is_odd(nums[i + 1]):
            char_list[i + 1] = 'x'
        else:
            char_list[i + 1] = '+'
    return char_list[1:]
    
n = int(input())
nums = list(map(int,input().split()))
print(''.join(get_odd_expression()))