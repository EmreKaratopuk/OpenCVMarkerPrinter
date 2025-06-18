import cv2
import cv2.aruco as aruco

# Choose the correct dictionary for your ArUco markers
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_1000)

# Initialize the detector parameters
parameters = aruco.DetectorParameters()

# Use webcam (change to a file path if you want to use an image)
frame = cv2.imread('x')

# Convert to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Detect ArUco markers
detector = aruco.ArucoDetector(aruco_dict, parameters)
corners, ids, _ = detector.detectMarkers(gray)

# Draw markers and their IDs
if ids is not None:
    aruco.drawDetectedMarkers(frame, corners, ids)
else:
    cv2.putText(frame, "No ArUco markers found", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Show result
cv2.imshow('ArUco Detection', frame)

if cv2.waitKey(0) & 0xFF == ord('q'):
    exit()

cv2.destroyAllWindows()
