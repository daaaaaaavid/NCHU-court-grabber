import numpy as np

try :
    from PIL import Image
except ImportError:
    import Image

def main():
    global visit , boundary , count , valid , x , y ,invalid_num , array 
    
    image = Image.open('captcha.png')
    array = np.array(image)          # array is a numpy array 
    y,x,z = array.shape
    invalid_num = array[0][0][0]
    
    visit = [[0 for i in range(x)]for j in range(y)]
    boundary = [[0,0,x,y]for i in range(10)]
    count = 0
    
    for i in range(y):
        for j in range(x):   
            valid = 0
            if(visit[i][j] == 0 and array[i][j][0] != invalid_num):
                try:
                    find(i,j)
                except:
                    return False
                if(valid > 40):
                    count += 1
                else:
                    boundary[count][0] = 0
                    boundary[count][1] = 0
                    boundary[count][2] = x
                    boundary[count][3] = y
                    
    boundary = sorted(boundary,key = lambda x : x[2])
    
    """
    for i in range(5):
        print(boundary[i])
                  
    
    new_array = np.zeros((y,x,3))
    x_start = 5
    y_start = 5
    for i in range(5):
            for x in range(boundary[i][2],boundary[i][0]):
                y_start = 5
                for y in range(boundary[i][3],boundary[i][1]):
                    new_array[y_start][x_start][0] = array[y][x][0]
                    new_array[y_start][x_start][1] = array[y][x][1]
                    new_array[y_start][x_start][2] = array[y][x][2]
                    y_start += 1
                x_start += 1
            x_start += 5                                        """
    for i in range(5):
        new_array = np.zeros((30,30,3))
        new_x = 3
        new_y = 3
        for x in range(boundary[i][2],boundary[i][0]):
            new_y = 3
            for y in range(boundary[i][3],boundary[i][1]):
                try:
                    new_array[new_y][new_x][0] = array[y][x][0]
                    new_array[new_y][new_x][1] = array[y][x][1]
                    new_array[new_y][new_x][2] = array[y][x][2]
                    new_y += 1
                except :
                    return False
            new_x += 1
            
        new_image = Image.fromarray((new_array * 255).astype(np.uint8))
        filename = 'new_captcha' + str(i) + '.png'
        new_image.save(filename)
        #new_image.show()
    return True
def find(a,b):
    global valid
    visit[a][b] = 1
    if(a > boundary[count][1]):
        boundary[count][1] = a
    if(a < boundary[count][3]):
        boundary[count][3] = a
    if(b > boundary[count][0]):
        boundary[count][0] = b
    if(b < boundary[count][2]):
        boundary[count][2] = b
    if(a-1 >= 0 and visit[a-1][b] == 0 and (array[a-1][b][0] < invalid_num-2 or array[a-1][b][0] > invalid_num+2)):
        valid += 1
        find(a-1,b)
    if(b-1 >= 0 and visit[a][b-1] == 0 and (array[a][b-1][0] < invalid_num-2 or array[a][b-1][0] > invalid_num+2)):
        valid += 1
        find(a,b-1)
    if(a+1 < y and visit[a+1][b] == 0 and (array[a+1][b][0] < invalid_num-2 or array[a+1][b][0] > invalid_num+2)):
        valid += 1
        find(a+1,b)
    if(b+1 < x and visit[a][b+1] == 0 and (array[a][b+1][0] < invalid_num-2 or array[a][b+1][0] > invalid_num+2)):
        valid += 1
        find(a,b+1)

if __name__ == '__main__':
    main()