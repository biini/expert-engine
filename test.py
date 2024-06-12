# 주어진 문자열
text = "hello world hello python hello code"
# 각 단어의 빈도수를 계산하여 딕셔너리에 저장
word_count = {}

# 문자열을 공백으로 분리하여 단어 리스트를 생성
words = text.split()
# 각 단어의 빈도수 계산
for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else: 
        word_count[word] = 1

# 결과 출력
print(word_count)