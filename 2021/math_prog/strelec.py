import time
board_height, board_width = input("").split(" ")[0:2]
word = input("")
start = time.perf_counter()
board = []

max_height = int(board_height) - 1
max_width = int(board_width) - 1

for rows in range(int(board_height)):
    cols = list(input(""))
    board.append(cols)

first_char = word[0]
paths = []
word = word[1:]

for height in range(len(board)):
    for width in range(len(board[height])):
        if board[height][width] == first_char:
            paths.append([[height, width]])


if not paths:
    print("0")
    exit()

for char_index in range(len(word)):
    for path_index in range(len(paths)):
        path = paths[path_index] 
        point = path[-1]
        distance = 1
        posibilities = [
            [point[0]+distance, point[1]+distance] if point[0] < max_height and point[1] < max_width else [],
            [point[0]-distance, point[1]-distance] if point[0] > 0 and point[1] > 0 else [],
            [point[0]+distance, point[1]-distance] if point[0] < max_height and point[1] > 0 else [],
            [point[0]-distance, point[1]+distance] if point[0] > 0 and point[1] < max_width else [],
        ]
        while posibilities != [[], [], [], []]:
            for posibility in posibilities:
                if not posibility:
                    continue
                if posibility == point:
                    continue
                if board[posibility[0]][posibility[1]] == word[char_index]:
                    temp = path.copy()
                    temp.append(posibility)
                    paths.append(temp)
            
            distance+= 1
            last= distance-1
            posibilities = [
                [point[0]+distance, point[1]+distance] if point[0]+last < max_height and point[1]+last < max_width else [],
                [point[0]-distance, point[1]-distance] if point[0]-last > 0 and point[1]-last > 0 else [],
                [point[0]+distance, point[1]-distance] if point[0]+last < max_height and point[1]-last > 0 else [],
                [point[0]-distance, point[1]+distance] if point[0]-last > 0 and point[1]+last < max_width else [],
            ]

    temp = []
    for path_index in range(len(paths)):
        if char_index+2 == len(paths[path_index]):
            temp.append(paths[path_index])

    paths = temp

print(len(paths) % (10**9 + 7))
print(time.perf_counter()-start)
