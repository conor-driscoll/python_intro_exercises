info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

# My solution without using str.replace():
# info_list = list(info)
# colon_count = info_list.count(':')
# colon_location_list = []
# colon_location = 0
# for i in range(0, colon_count):
#     colon_location = info.find(':', colon_location)
#     colon_location_list.append(colon_location)
#     colon_location = colon_location + 1
# for i in colon_location_list:
#     info_list[i] = '+'
# edited_info = ''.join(info_list)
# print(edited_info)

# Launch School's solution without using str.replace():
# parts = info.split(':')
# result = '+'.join(parts)
# print(result)

print(info.replace(':', '+'))