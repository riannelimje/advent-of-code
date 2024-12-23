# what is a christmas tree picture???
with open('input.txt', 'r') as file:
    data = file.read().strip().splitlines()

x = 101 #wide - col
y = 103 #tall - row

# assuming that the earliest position where robots do not overlap is valid as the solution
for i in range(1,x*y+1):
    finalPos = set()
    for line in data:
        p,v = line.split()
        px =  int(p.split(',')[0][2:])
        py = int(p.split(',')[1])
        vx =  int(v.split(',')[0][2:])
        vy = int(v.split(',')[1])

        px = (px + i * vx) % x
        py = (py + i * vy) % y
        finalPos.add((px,py))

    if len(finalPos) == len(data):
        print(f"found it at {i}")
        break

# lemme try to visualise how the christmas tree looks like 
grid = [[" " for  _ in range(x)] for _ in range(y)]
for px,py in finalPos:
    grid[py][px] = '#'

for row in grid:
    print("".join(row))

                                                       ###############################               
                                  #                    #                             #               
                                                       #                             #               
                                                       #                             #               
                                                       #                             #               
                                                       #              #              #               
#                                                      #             ###             #               
        #                                              #            #####            #               
           #                #                    #     #           #######           #               
           #                                           #          #########          #    #          
                                             #         #            #####            #               
                                                       #           #######           #               
                                                       #          #########          #               
                    #                        #         #         ###########         #               
                                                       #        #############        #               
                                                       #          #########          #               
                                                       #         ###########         #               
                                                       #        #############        #               
                                                       #       ###############       #     #         
                                                       #      #################      #              #
                                                       #        #############        #               
                 #                                     #       ###############       #    #          
                                        #              #      #################      #               
                                                       #     ###################     #    #          
                                                       #    #####################    #              #
                #              #                       #             ###             #               
                                              #        #             ###             #               
                   #                                   #             ###             #               
                                   #                   #                             #               
                                                       #                             #     #         
         # #                                           #                             #               
                    #                                  #                             # #             
                                                       ###############################     