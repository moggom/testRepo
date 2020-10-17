def solution(mylist):
    answer = []
    # mylist 안에 item들마다 한번씩 실행
    for item in mylist:
        answer.append(len(item))
    
    return answer
