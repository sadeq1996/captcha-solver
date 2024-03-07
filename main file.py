import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd =\
                                      r"C:\Program Files\Tesseract-OCR\tesseract.exe"


img= cv2.imread("3_c.jpg")

# resized_img = cv2.resize(img, (100, 100))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


blur = cv2.GaussianBlur(gray, (5, 5),10)


edges = cv2.Canny(blur, 20, 20)

ret, thresh = cv2.threshold(blur, 0, 10, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
max_area = 0
best_cnt = None
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > max_area:
        max_area = area
        best_cnt = cnt
        
x, y, w, h = cv2.boundingRect(best_cnt)
cv2.rectangle(img, (x, y), (x + w, y + h), (0,255, 0), 0)


crop_img = img[y:y+h, x:x+w]
# *Apply additional preprocessing to ROI
gray_crop = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
blur_crop = cv2.GaussianBlur(gray_crop, (3, 3), 0)
thresh_crop = cv2.adaptiveThreshold(blur_crop, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)



config = r"C:\Program Files\Tesseract-OCR\tessdata"
text = pytesseract.image_to_string(thresh_crop, lang='Eng', config=config)


print(text)

cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

