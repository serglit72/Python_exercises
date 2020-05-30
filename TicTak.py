from random import randint
from IPython.display import clear_output


def display(grid,player_a,player_b):
    
    print("_1_"+'|'+"_2_"+'|'+"_3_")
    print("_4_"+'|'+"_5_"+'|'+"_6_"+"      Player A  ("+player_a+") uses key "+marker+" !! ")
    print(" 7 "+'|'+" 8 "+'|'+" 9 "+"      Player B  ("+player_b+") uses key "+ marker_b )
    print("________________________________")
    print("LETS PLAY on {}x{} !!!".format(grid,grid))
    print("Use digit keys for input your step!")
   
    
def marker():
    marker = ""
    marker_b = ""
    while marker !='X' or marker !=int("0"):
        marker = input("Player A should choose a marker X or 0 : ")
        if marker == "X":
            marker_b = "0"
            break
        elif marker == "0":
            marker_b = "X"
            break
    return marker, marker_b  




# def who_start(player_a ,player_b):
#     dice = {"n1":0,
#             "n2":0}
    
#     for i in range(1,3):
#         if dice["n1"] == dice["n2"]:
#             if i == 1:
#                 print("{} should click 'Whitespace' button".format(player_a))
#                 if input(" "):
#                     dice["n1"] = randint(1,6)
#                     continue
#             elif i == 2:
#                 print("{} should click 'Whitespace' button".format(player_b))
#                 if input(" "):
#                     dice["n2"] = randint(1,6)
            
#         if dice["n1"] > dice["n2"]:
#             result = 1
#             print("{} is going to start".format(player_a))
#             return result 
        
#         elif int(dice[0]) < int(dice[1]):
#             result = 2 
#             print("{} is going to start".format(player_b))
#             return result
#         else:
#             print("Start again")
#     else:
#         return result  
        
def game(player_a,player_b, marker, marker_b):
        i = 1
        j = 1
        positions = []
        steps = list(range(11,20))
    # while j<10:
        while (steps[0]!=steps[3]!=steps[6] or \
                steps[1]!=steps[4]!=steps[7] or \
                steps[2]!=steps[5]!=steps[8] or \
                steps[0]!=steps[1]!=steps[2] or \
                steps[3]!=steps[4]!=steps[5] or \
                steps[6]!=steps[7]!=steps[8] or \
                steps[0]!=steps[4]!=steps[8] or \
                steps[2]!=steps[4]!=steps[6]) or j<10 :
            
            if i%2==0:
                s = input("Player {} with {} turn : ".format(player_b,marker_b))
                if s not in positions:
                    steps[int(s)-1] = marker_b
                    positions.append(s)
                    i+=1
                    j+=1
                elif s in positions:
                    print("Warning!!!!")
                    continue
            else:    
                s = input("Player {} with {} turn : ".format(player_a,marker))
                if s not in positions:
                    steps[int(s)-1] = marker
                    positions.append(s)
                    i+=1
                    j+=1
                elif s in positions:
                    print("Warning!!!!")
                    continue
            
        else:
            print("nobody won- try again",net(steps))

        # steps[0]==steps[3]==steps[6] or \
        #     steps[1]==steps[4]==steps[7] or \
        #     steps[2]==steps[5]==steps[8] or \
        #     steps[0]==steps[1]==steps[2] or \
        #     steps[3]==steps[4]==steps[5] or \
        #     steps[6]==steps[7]==steps[8] or \
        #     steps[0]==steps[4]==steps[8] or \
        #     steps[2]==steps[4]==steps[6]
        # print("i won",net(steps))

    
        print(player_a+" won",net(steps))   
        return(steps)

def net(steps):
    print("_"+str(steps[0])+"_|_"+str(steps[1])+"_|_"+str(steps[2])+"_")
    print("_"+str(steps[3])+"_|_"+str(steps[4])+"_|_"+str(steps[5])+"_")
    print(" "+str(steps[6])+" | "+str(steps[7])+" | "+str(steps[8])+" ")



#Here are instruction for the DEFs
player_a = input("Give me a Player A name? : ")
player_b = input("Give me a Player B name? : ")
marker,marker_b = marker()
# who_start(player_a,player_b)

# print(display(3,player_a,player_b))
game(player_a,player_b, marker, marker_b)