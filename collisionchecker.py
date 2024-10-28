import pygame
def collision(cordinates,rectangle_list,surface_hight,surface_width):             #this function finds if a coordinate is inside a
    cor_rect=pygame.Rect(cordinates[0],cordinates[1],surface_hight,surface_width) #rectangle by converting the single coordinate in
    is_in=pygame.Rect.collidelist(cor_rect,rectangle_list)                        #list into rectangle and then passing it to collidelist function
    if is_in==-1:
        return False
    else:
        return True
def collide(coordinate,cor_rect_trans_list,rect_hight_list,rect_width_list):
    list_rect=[]
    try:
        cor_rect_trans_list =list(cor_rect_trans_list)
        cor_rect_trans_list.pop(0)
    except :
        print("error occured")
    for rect in cor_rect_trans_list:
        list_rect.append(pygame.Rect(rect[0],rect[1],rect_hight_list,rect_width_list))

    return collision(coordinate,list_rect,rect_hight_list,rect_width_list)
"""this function finds if a coordinate in list is inside a list which contain coordinates of rectangle by converting list 
    of coordinates of rectrangles into list of rectangles and then passing them to collision function above """