def find_relative_distance(index1,index2):

    file = open('')

    mylist=list(file)

    for line in mylist:
        line_values = line.split(',')
        index=int(line_values[5])
        if index == index1:
            x0=float(line_values[2])
            y0=float(line_values[3])
        if index == index2:
            x1=float(line_values[2])
            y1=float(line_values[3])
            
    print('shift in x: ',x1-x0,'\nshift in y: ',y1-y0)
    file.close()
    return

find_relative_distance(1047,1048)