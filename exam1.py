score = [70, 80, 90, 87]
tot = sum(score)
num = len(score)
avg = sum(score) / len(score)
maxScore = max(score)
minScore = min(score)

print("score :", score)
print("총점 : {}, 평균 : {:.1f}".format(tot, avg))
print("최고점수 : {}, 최저점수 : {}".format(maxScore, minScore))
