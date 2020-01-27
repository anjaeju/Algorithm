import numpy as np
import matplotlib.pyplot as plt
import PIL
from PIL import Image
from PIL import ImageFilter

# 프로그래머를 위한 선형대수 2챕터 2-6에 나오는 실험 내용.
# gradation matrix를 곱해서 납작하게 눌리지 않는 사상으로 변환 후, 다시 복원

img = np.array(Image.open('C://Users//anjae//Documents//example.jpg').resize((300, 300), PIL.Image.BILINEAR))[:,:,0]

X = np.array(img)                # origin image

A = np.random.randn(*X.shape)         # gradation matrix

Y = np.matmul(X, A)

Z = np.matmul(Y, np.linalg.inv(A))         # resotred image from O.O.F image

print(X[0])
print(Y[0])
print(A.T[0])

plt.title('Before gradation')
plt.imshow(X)
plt.show()

plt.title('After gradtion')
plt.imshow(Y)
plt.show()

plt.title('Restored')
plt.imshow(Z)
plt.show()
