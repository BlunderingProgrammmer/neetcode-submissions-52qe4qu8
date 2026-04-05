class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.snake_body =  collections.deque([(0,0)])
        self.snake_set = {(0,0)}
        self.directions = {'U': [-1,0],'D': [1,0],'L': [0,-1],'R': [0,1]}
        self.score = 0
    def move(self, direction: str) -> int:
        r,c = self.snake_body[-1]# getting og head
        new_r,new_c = r + self.directions[direction][0],c + self.directions[direction][1] #calc new position for head
        if not (0 <= new_r < self.height and  0 <= new_c < self.width):
            return -1
        #before collision check remove tail from hash set to ensure head can move to tail old position
        tail = self.snake_body[0]
        self.snake_set.remove(tail)
        #collision check
        if (new_r,new_c) in self.snake_set:
            return -1
        if_flag = False #proud of this one hahahah
        if self.food:
            food_r ,food_c = self.food[0]
            if (new_r,new_c) == (food_r,food_c):
                self.score +=1
                self.snake_set.add(tail)
                self.snake_body.append((new_r,new_c))
                self.snake_set.add((new_r,new_c))
                del self.food[0]
                if_flag = True
        if not if_flag:
            self.snake_body.popleft()
            self.snake_body.append((new_r,new_c))
            self.snake_set.add((new_r,new_c))
            if_flag = False
        

        return self.score
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
