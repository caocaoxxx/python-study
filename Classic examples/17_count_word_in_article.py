word_count ={}
with open('./17article.txt','r',encoding='utf-8') as file:
    for line in file:
        line=line[:-1]
        words = line.split()#去掉空格是为了确保在处理每一行文本时，
        #能够正确地分割单词并统计它们的出现次数。虽然原文件文本是正常的英文文本，但去掉行末的空格可以避免不必要的空格影响单词的统计
        for word in words:
            if word not in word_count:
                word_count[word]=0
            word_count[word]+=1
print(word_count.items())
print(sorted(
    word_count.items(),#返回一个键值对的列表
    key = lambda x:x[1],
    reverse=True
)[:10])
