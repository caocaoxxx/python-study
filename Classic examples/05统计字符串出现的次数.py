s = 'HelloPython,HelloJava,hellophp'
word = input('请输入要统计的字符:')

print(s.upper().count(word))
print('{0}在{1}中出现了{2}次'.format(word,s,s.upper().count(word)))
