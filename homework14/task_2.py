def midpoint(tuple_1,tuple_2):
    mid_x=(tuple_1[0]+tuple_2[0])/2
    mid_y=(tuple_1[1]+tuple_2[1])/2
    return mid_x,mid_y
def main():
    print(midpoint((3,5),(5,7)))
    print(midpoint((10,5),(-4,-11)))
if __name__=='__main__':
    main()