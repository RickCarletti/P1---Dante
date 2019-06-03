dd, mm, aa = map(str, input().split('/'))

print('/'.join([mm,dd,aa]))
print('/'.join([aa,mm,dd]))
print('-'.join([dd,mm,aa]))
