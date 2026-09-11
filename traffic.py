from ultralytics import YOLO 
import cv2 
# YOLO model load
model = YOLO("yolov8n.pt")
#ideo/camera 
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
     ret, frame = cap.read()

     if not ret: 
         break
      # Vehicle detection 
     results = model(frame) 
     # Detected objects ke boxes draw 
     annotated_frame = results[0].plot() 
     cv2.imshow("Real-Time Traffic Detection",
            annotated_frame)
 # Q dabakar exit 
     if cv2.waitKey(1) & 0xFF == ord("q"): 
       break 
cap.release()
cv2.destroyAllWindows()