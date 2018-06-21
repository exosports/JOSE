import jose
import os
from astropy.io import fits as pyfits
import matplotlib.pyplot as plt
import numpy as np

print('hello tests')
print(os.getcwd())

exampleDir = 'images'
curvedFrame = pyfits.open(os.path.join(exampleDir, 'ex4.fits'))[0]

Q = curvedFrame.header.get('EPADU')
rn = curvedFrame.header.get('RDNOISE') / Q
left_bound = 240
right_bound = 270
varim = np.abs(curvedFrame.data) / Q + rn**2

traceCenters = jose.find_centers(curvedFrame.data, varim, left_bound, right_bound)

plt.imshow(curvedFrame.data)
plt.plot(traceCenters, list(range(len(traceCenters))))
plt.show()

print('stuff')
