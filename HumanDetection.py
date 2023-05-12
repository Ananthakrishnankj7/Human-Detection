import cv2
import mediapipe as mp
detected_poses = []

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture(0)

while True:
    x, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = pose.process(imgRGB)
    # print(type(results.pose_landmarks))
    if results.pose_landmarks:
        print("Human Detected")
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, i_am_not_here = img.shape
            # print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    if cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) <1:
        break
cv2.destroyllAllWindows()


# import cv2
# import mediapipe as mp
#
# mpDraw = mp.solutions.drawing_utils
# mpPose = mp.solutions.pose
# pose = mpPose.Pose()
#
# cap = cv2.VideoCapture(0)
#
# while True:
#     x, img = cap.read()
#
#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#
#     results = pose.process(imgRGB)
#
#     if results.multi_pose_landmarks:
#         detected_poses = {}
#         for idx, pose_landmarks in enumerate(results.multi_pose_landmarks):
#             pose_info = {}
#             lm_list = []
#             for id, lm in enumerate(pose_landmarks.landmark):
#                 h, w, _ = img.shape
#                 cx, cy = int(lm.x * w), int(lm.y * h)
#                 lm_list.append((cx, cy))
#                 cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
#
#             pose_info['landmarks'] = lm_list
#             detected_poses[idx] = pose_info
#
#             mpDraw.draw_landmarks(img, pose_landmarks, mpPose.POSE_CONNECTIONS)
#
#             # Draw bounding box around the pose
#             bbox = cv2.boundingRect(pose_landmarks.landmark)
#             cv2.rectangle(img, (bbox[0] - 10, bbox[1] - 10), (bbox[0] + bbox[2] + 10, bbox[1] + bbox[3] + 10),
#                           (0, 255, 0), 2)
#
#         # Process detected poses in the dictionary 'detected_poses'
#         for pose_id, pose_info in detected_poses.items():
#             landmarks = pose_info['landmarks']
#             # Process or analyze the landmarks of each pose as needed
#
#     cv2.imshow("Image", img)
#     cv2.waitKey(1)
#     if cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) < 1:
#         break
#
# cv2.destroyAllWindows()
