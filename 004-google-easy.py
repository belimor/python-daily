#!/usr/bin/python3

# This problem was asked by Google.
# Given two rectangles on a 2D graph, 
# return the area of their intersection. 
# If the rectangles don't intersect, return 0.

#For example, given the following rectangles:
#{
#    "top_left": (1, 4),
#    "dimensions": (3, 3) # width, height
#}
#and
#{
#    "top_left": (0, 5),
#    "dimensions": (4, 3) # width, height
#}
#return 6.

def intersection_area(rec1, rec2):
    
    x1,y1 = rec1["top_left"]
    w1,h1 = rec1["dimensions"]
    x2,y2 = rec2["top_left"]
    w2,h2 = rec2["dimensions"]
    
    # compute bottorm-right corners

    x1_br,y1_br = x1+w1,y1-h1
    x2_br,y2_br = x2+w2,y2-h2

    # find overlap in x y dimensions

    overlap_x = max(0, min(x1_br,x2_br) - max(x1,x2))
    overlap_y = max(0, min(y1,y2) - max(y1_br,y2_br))

    # calculate intersrection area

    return overlap_x * overlap_y


rec1 = {
        "top_left": (1, 4),
        "dimensions": (3, 3) # width, height 
        }
rec2 = {
        "top_left": (0, 5),
        "dimensions": (4, 3) # width, height 
        }
print(intersection_area(rec1, rec2))

