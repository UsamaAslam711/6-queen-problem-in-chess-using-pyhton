
board1 = [1, 0, 2, 1, 4, 4]
board2 = [3, 1, 3, 0, 3, 2]
board3 = [0, 2, 1, 2, 5, 1]
board4 = [3, 0, 1, 0, 0, 1]

def AttackingPair(board):
    global total_count, queen
    list = []
    for i in range(0, 6):
        list.append([board[i], i])

    while (list):
        count = 0
        i, j = list.pop(0)
    # Row me check krne k liye
        if (j < 5):
            for x in range(j+1, 6):
                if [i, x] in list:
                    count += 1
                    total_count += 1
    # Diagonal me check krne k liye
        i1, j1 = i, j
        while (i1 <= 5 and j1 <= 5):
            i1 = i1 + 1
            j1 = j1 + 1
            if [i1, j1] in list:
                count = count + 1
                total_count =  total_count + 1
    # Non Diagonal me check krne k liye
        i1, j1 = i, j
        while (i1 >= 0 and j1 <= 5):
            i1 -= 1
            j1 += 1
            if [i1, j1] in list:
                count += 1
                total_count += 1
        print('Queen '+ str(queen) + ' :', count)
        queen += 1
    return (total_count)


queen = 0
total_count = 0


attacking_pair = AttackingPair(board4)
print('Total Board Attacks :', attacking_pair)
