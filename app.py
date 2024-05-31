import cv2

image = cv2.imread('car.jpg')
carros = cv2.CascadeClassifier('cars.xml')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cars = carros.detectMultiScale(gray,1.1,1)

for (x,y,w,h) in cars:
  cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0) , 2)

cv2.imshow("autos detectados ",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

