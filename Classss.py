class Line:
    
    def __init__(self,coor1,coor2):
    
        self.coor1 = coor1
        self.coor2 = coor2
        print(coor1)
        print(coor2)
        
    
    def distance(self):
        dist = float((self.coor2[1]-self.coor1[1])**2 - (self.coor2[0]-self.coor1[0])**2)**0.5

        return dist
    
    def slope(self):
        sl = (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])
        
        return sl

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print("distance = ", li.distance())
print("slope = ", li.slope())