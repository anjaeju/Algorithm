def get_idx(map, number):
    return next( [i,j] for i, line in enumerate(map)
               for j, x in enumerate(line) if x == number)

def get_distance(cur, target):
    x1, y1 = cur[0], cur[1]
    x2, y2 = target[0], target[1]
    return (x2-x1)**2 + (y2-y1)**2

def solution(numbers, hand):
    map_ =[[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         ['*', 0, '#']]
    
    cur_left_hand = '*'
    cur_right_hand = '#'
    
    answer = ''
    
    for each in numbers:
        each_position = get_idx(map_, each)
        
        if each_position[1] == 0:
            answer += 'L'
            cur_left_hand = each
        
        elif each_position[1] == 2:
            answer += 'R'
            cur_right_hand = each
        
        else:
            left_hand_position = get_idx(map_, cur_left_hand)
            right_hand_position = get_idx(map_, cur_right_hand)
            
            left_distance = get_distance(left_hand_position, each_position)
            right_distance = get_distance(right_hand_position, each_position)
            
            if left_distance == right_distance:
                if hand[0] == 'l':
                    answer += 'L'
                    cur_left_hand = each
                else:
                    answer += 'R'
                    cur_right_hand = each
                    
            elif left_distance < right_distance:
                    answer += 'L'
                    cur_left_hand = each
            else:
                answer += 'R'
                cur_right_hand = each
                
    return answer
