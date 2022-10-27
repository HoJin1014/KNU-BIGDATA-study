import cv2
import numpy as np

img1=cv2.imread(r"C:\Users\USER\vscode\lg_project\rose.JPG")
cv2.imshow('rose', img1)
cv2.waitKey(0)
cv2.destroAllwindows()

# 이미지 파일을 jpeg 형식으로 쓰기
# (이미지명, Data, [형식, 퀄리티])
# cv2.imwrite(r"C:\Users\USER\vscode\lg_project\rose.jpg.jpg", img1, [cv2.IMWRITE_JPEG_QUALITY, 95])
# cv2.imwrite(r"C:\Users\USER\vscode\lg_project\rose.png.png", img1, [cv2.IMWRITE_COMPRESSION, 3])

empty_mat = np.empty((500, 500), np.float32)
zeros_mat = np.zeros((500, 500))
ones_mat = np.ones((500, 500))
ones_mat_int = np.ones((500, 500), np.uint8)

cv2.imshow('empty_mat', empty_mat)
cv2.imshow('zeros_mat', zeros_mat)
cv2.imshow('ones_mat', ones_mat)
cv2.imshow('ones_mat_int', ones_mat_int)
cv2.waitKey(0)
cv2.destroAllwindows()

zeros_mat.fill(10.)
ones_mat_int.fill(128)
cv2.imshow('zeros_mat_10', zeros_mat)
cv2.imshow('ones_mat_int', ones_mat_int)
cv2.waitKey(0)
cv2.destroAllwindows()

my_mat = np.array([[255, 255, 0, 0, 255], [255, 255, 0, 0, 255, 255]])
my_mat2 = np.array([[1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1]])

print('img.dtype = ', my_mat.dtype) # 자료형
print('img.ndim = ', my_mat.ndim) # 차원 수
print('img.shape = ', my_mat.shape) # 이미지의 모양

# -----------------------------------------------------
# import cv2
# import numpy as np

# img = cv2.imread()
# -----------------------------------------------------

# 도형 그리기
## cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
# cv2.rectangle(rgb_img, (10, 10), (100, 100), (0, 0, 255), thickness=1)

## cv2.line(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
# cv2.line(rgb_img, (10, 300), (100, 300), (0, 255, 0), thickness=3)

## cv2.putText(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
# cv2.putText(rgb_img, 'hello', (200, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255))

## cv2.circle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
# cv2.circle(rgb_img, (300, 300), 20, (0, 255, 255))

# points1 = np.array([[350, 350], [360, 410], [370, 420], [450, 500]], np.uint32)
# cv2.polylines(rgb_img, [points1], True, (255, 0, 0))

# cv2.imshow('img', rge_img)
# -------------------------------------------------------------------------------------------

# Geometric transformation 기하학적 변환
# 영상의 크기, 위치를 변화시키거나 회전시키는 등의 변환을 의미(스케일링, 회전, 뒤집기 가능)

# Resize

# affine transform 아핀 변환 - 평행을 유지하면서 이동, 회전, 크기 등을 변환할 수 있다.
# 6개 식이 필요 - 매칭되는 3개의 쌍이 있으면 행렬을 구할 수 있다.
# 중심점 기준으로 회전, wrapAffine 함수로 변환 행렬을 적용하여 affine 변환을 진행
# rot_mat = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
# rot_mat_0 = cv2.getRotationMatrix2D((0, 0), 45, 1.0)
# lena_45 = cv2.wrapAffine(lena_img, rot_mat, (w, h))
# lena_45_0 = cv2.wrapAffine(lena_img, rot_mat_0, (w, h))
# cv2.imshow('lena_45', lena_45)
# cv2.imshow('lena_45_0', lena_45_0)
# cv2.waitKey(0)
# cv2.destroAllwindows()

