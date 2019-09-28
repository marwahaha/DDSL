from airfoil_NUFT import *
import time

print('Now processing rectangle shapes...')

# Convert all airfoils in airfoil-data
directory='Rectangle Test'
i=0
start=time.time()
for root, dirs, files in os.walk(directory):
    for rectangle in files:
        # Create save file name
        case_end = 0
        for index in range(len(rectangle)):
            if rectangle[index] == '_':
                case_end = index
                break
        rectangle_name = rectangle[0:4] + rectangle[5:case_end]
        save_file='processed_data/'+rectangle_name+'.pt'
        if not os.path.exists(save_file):
            airfoil_phys(rectangle, res=(224,224), device='cpu', save_name=save_file, grad=False)
        i=i+1

        end=time.time()
        print(str(i)+' rectangles processed! Time elapsed: '+str(end-start))
        start=time.time()

print('Processing complete!')

