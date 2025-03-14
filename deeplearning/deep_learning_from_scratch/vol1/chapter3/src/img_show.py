import sys, os
sys.path.append(os.pardir)
import numpy as np
from mnist import load_mnist
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()
    
if __name__ == "__main__":
    (x_train, t_train), (x_test, t_test) = \
        load_mnist(flatten=True, normalize=False)
        
    img = x_train[5]
    label = t_train[5]
    
    img = img.reshape(28, 28)
    
    img_show(img)
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.save("mnist_sample.png")    
