def compute_score():
    scores=[]
    with open('./15输出学生成绩.txt','r',encoding='utf-8') as file:
        for line in file:
            line=line.strip()
            fileds = line.split(',')
            scores.append(int(fileds[-1]))
    max_score = max(scores)
    min_score = min(scores)
    avg_score = sum(scores) / len(scores)
    return max_score, min_score, avg_score

max_score, min_score, avg_score = compute_score()

print(f'max_score: {max_score}\nmin_score: {min_score}\navg_score: {avg_score}')
print(f'max_score: {max_score}, min_score: {min_score}, avg_score: {avg_score}')