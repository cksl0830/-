def solution(new_id):
    remove = '~!@#$%^&*()=+[{]}:?,<>/'
    # 1단계
    new_id = new_id.lower()

    # 2단계
    answer = ""
    for i in new_id:
        if i not in remove:
            answer += i

    # 3단계
    while ".." in answer:
        answer = answer.replace('..', '.')

    # 4단계
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]

    # 5단계
    if answer == '':
        answer += 'a';

    # 6단계
    if len(answer) > 15:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]

    # 7단계
    if len(answer) < 3:
        answer = answer + answer[-1] * (3 - len(answer))

    return answer


// 다른 사람의 풀이 (정규삭)

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st


