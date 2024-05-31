import cv2

carros = cv2.CascadeClassifier('cars.xml')

cap = cv2.VideoCapture('video01.mp4')

if not cap.isOpened():
    print("Error al abrir el archivo de video.")
    exit()

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cars = carros.detectMultiScale(gray, 1.1, 1)
    
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv2.imshow("Autos detectados", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()