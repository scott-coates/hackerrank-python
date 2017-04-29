import requests

x = 1000000

x = 10

#
# def is_cool(number):
#     num_str = str(number)
#     num_parts = [int(i) for i in num_str]
#     total = 0
#     for n in num_parts:
#         total += (n ** 2)
#
#     if total == 1:
#         ret_val = True
#     elif total == 4:
#         ret_val = False
#     else:
#         ret_val = is_cool(total)
#
#     return ret_val
#
#
# print(is_cool(23))
#
# sum_cool = []
# for i in range(1, x + 1):
#     if is_cool(i):
#         sum_cool.append(i)
#     print('done', i)
#
# sum_total = sum(sum_cool)
#
# print(sum_total)
# total = sum_total

total = 70601040511

headers = {'X-COOL-SUM': total}
code = ''
for i in range(1, 100+1):
    response = requests.post('http://dev.getethos.com/code{0}'.format(i), headers=headers)
    print(response)
    if response.status_code != 404:
        code += response.text

print(code)
