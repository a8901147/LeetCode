class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        inf = 2147483647
        empty_room = 0
        gates = []
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    gates.append([r,c,0]) # [row,col,distance]
                elif rooms[r][c] == inf:
                    empty_room += 1
    
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        while gates and empty_room:
            next_gates = []
            for gate_row, gate_col, distance in gates:
                for x, y in dirs:
                    room_x, room_y = gate_row+x, gate_col+y
                    if room_x<0 or room_y<0 or room_x>=len(rooms) or room_y>=len(rooms[0]) or rooms[room_x][room_y] != inf:
                        continue
                    rooms[room_x][room_y] = distance+1
                    next_gates.append([room_x,room_y,distance+1])
                    empty_room -= 1
            gates = next_gates  

        return rooms      