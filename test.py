import sys

print('This works outside  IDLE! \U0001F44D')
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

print('This works in IDLE too! \U0001F44D'.translate(non_bmp_map))
print('asfasfa'.translate(non_bmp_map))
