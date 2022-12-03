# https://school.programmers.co.kr/learn/courses/30/lessons/42577
def make_deep_dict(phone, idx, dixt):
    make_deep_dict(phone, idx-1, dixt)
    dixt = {phone[idx]:dict()}
    return 
def solution(phone_book):
    answer = True
    all_dict = dict()
    # for phone in phone_book:
    #     # if all_dict.get(phone) == None:
    #     for num in range(len(phone)):
    #         all_dict[phone[:num]] = 1
    for phone in phone_book:
        all_dict[phone[0]] = {
            phone[1]:{
                phone[2]:{
                    phone[3]
                }
            }
        }
        for number in phone:
            
    return answer

solution(["119", "97674223", "1195524421"])
solution(["123","456","789"])
solution(["12","123","1235","567","88"])