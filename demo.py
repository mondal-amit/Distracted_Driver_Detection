import cv2
import tensorflow as tf
import numpy as np

# Load trained model
model = tf.keras.models.load_model("models/distracted_driver_model.keras")

class_names = ["safe driving", "texting right", "talking right", "texting left",
               "talking left", "adjusting radio", "drinking", "reaching behind",
               "hair/makeup", "talking to passenger"]

cap = cv2.VideoCapture(0)  # webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img = cv2.resize(frame, (224, 224))
    img = np.expand_dims(img/255.0, axis=0)

    pred = model.predict(img, verbose=0)
    label = class_names[np.argmax(pred)]

    cv2.putText(frame, f"Prediction: {label}", (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Distracted Driver Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
