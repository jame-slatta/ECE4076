import numpy as np
Im1P1 = [40,30,20,30,20,10, 20, 10, 0]
Im1P2 = [25,40,25,25,30,25,25,25,25]
Im2P1 = [25,25,15,25,15,10,15,10,0]
Im2P2 = [20,20,20, 20,20,15, 20, 15, 5]

def calculate_ssd(img1, img2):
    
    return np.sum((np.array(img1, dtype=np.float32) - np.array(img2, dtype=np.float32))**2)
print(calculate_ssd(Im1P1, Im2P1))
print(calculate_ssd(Im1P1, Im2P2))
print(calculate_ssd(Im1P2, Im2P1))
print(calculate_ssd(Im1P2, Im2P2))