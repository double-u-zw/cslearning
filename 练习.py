#练习1:请利用print()输出1024 * 768 = xxx：
a=1024*768
print('1024*768=',a)

#练习2:请打印出以下变量的值：
n=123
f=456.789
s1='Hello,World'
s2='Hello,\'adam\''
s3=r'hello,"bart"'
s4=r'''hello,
Bob'''

print(n,f,s1,s2,s3)
print(s4)

#练习3:小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1=72
s2=85
r=(s2-s1)/s1

print(f'小明成绩提升了 {r*100:.1f}%')

#请用索引取出下面list的指定元素：
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Bob:
print(L[2][2])