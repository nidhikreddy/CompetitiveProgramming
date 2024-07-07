import sys
nums = [int(x) for x in input().split()]
product = nums[0] * nums[1] 
# print(product)
if product % 2 == 0:
    even_answer = product/2
    print( int(even_answer))
else:
    odd_product_semi = product - 1
    # print(odd_product_semi)
    odd_product = odd_product_semi / 2
    print( int(odd_product))
