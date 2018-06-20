import jose
import os
from astropy.io import fits as pyfits
import matplotlib.pyplot as plt

print('hello tests')
print(os.getcwd())

exampleDir = 'images'
curvedFrame = pyfits.open(os.path.join(exampleDir, 'ex3.fits'))[0]

traceCenters = jose.find_centers(curvedFrame.data)

plt.imshow(curvedFrame.data)
plt.plot(traceCenters, list(range(len(traceCenters))))
plt.show()

