import cv2
import numpy as np

D_2 = [[0, 128, 32, 160], [192, 64, 224, 96], [48, 176, 16, 144], [240, 112, 208, 80]]
img_name = input("Please the Image name that you want to dithering: ")
img = cv2.imread(img_name)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_size = img_gray.size
img_col_size = img_gray[0].size
img_row_size = int(img_size / img_col_size)
output_img = np.zeros((img_row_size, img_col_size))

for cur_row in range(img_row_size):
    for cur_col in range(img_col_size):
        if img_gray[cur_row][cur_col] > D_2[cur_row % 4][cur_col % 4]:
            output_img[cur_row][cur_col] = 255
        else:
            output_img[cur_row][cur_col] = 0

cv2.imwrite("A_" + img_name, output_img)
print("Already dithering %s" % (img_name), "by dithering matrix D_2.")

cv2.imshow("Origianl Image", img_gray)
cv2.imshow("New Image", output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()