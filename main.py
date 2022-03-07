#! C:/Python310/ python
import os
import re
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.use('Qt5Agg')


# Defines main
def main():
    print("main")
    arr = np.empty((9,50),str)

    for csv in os.listdir(os.getcwd()+'/data2'):
        if (re.search("Række.*\.csv", csv) != None):
            temp = np.genfromtxt("data2/"+csv, delimiter=";", dtype=str,skip_header=1)
            temp = np.array(np.array_split(temp,9,axis=1))[:,:,1:]
            arr = np.dstack((arr,temp))




    arr = np.transpose(arr[:,:,1:],(0,2,1))
    arr = np.core.defchararray.replace(arr,',', '.')
  
    arr = arr.astype('float64')

    # print(np.amax(arr))

    arr = np.mean(arr,axis=2)
    arr = np.rot90(arr)
    arr = np.flip(arr, axis=0)


    plt.imshow(arr, cmap="plasma")
    plt.gca().invert_yaxis()
    plt.title("Lydinterferens")
    plt.colorbar(label="dB")

    plt.show()

""" 
0th axis of arr is equivalent to x on the grid (from left to right) 
1st axis of arr is equivalent to y on the grid (from bottom to top)
2nd axis off arr is equivalent to time (ie. the individual 50 observations)    
"""

if __name__=="__main__":
    main()
