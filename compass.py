def direction(facing, turn):

    list_directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    turns = turn // 45
    start = list_directions.index(facing)
    end = (start + turns) % len(list_directions)
    
    return list_directions[end]


print(direction('S', 180))