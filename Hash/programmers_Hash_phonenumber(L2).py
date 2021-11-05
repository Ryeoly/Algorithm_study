def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

# def solution(phone_book):
#     phone_book.sort(key=lambda x : len(x))
#     for i in range(len(phone_book)):
#         for j in phone_book[i+1:]:
#             if phone_book[i] == j[:len(phone_book[i])]:
#                 return False
#     return True

# 전자는 효율성 테스트까지 모두 통과한 것
# 후자는 효율성 테스트 2개 맞고, 2개 틀린 것
# sort를 사용해서 푸는 방법을 똑같이 생각했음에도 반복문을 하나 없앨 수 있는
# 선택지가 가능했기에 두번째는 별로인 코드
# 숫자대로 sort되면 바로 앞에 있는 숫자만 확인하면 된다.