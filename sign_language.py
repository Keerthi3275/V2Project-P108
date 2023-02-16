import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

#Create a fingertips array with the values of finger tips.(As given in Specific task1)

thumb_tip= 4 #Assigning thumbtip variable

while True:
    ret,img = cap.read()
    img = cv2.flip(img, 1)
    h,w,c = img.shape
    results = hands.process(img)


    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            #accessing the landmarks by their position
            lm_list=[]
            for id ,lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)
            # #array to hold true or false if finger is folded (AS given in specific task 2)




                #writing condition to check if finger is folded i.e checking if finger tip starting value is smaller than finger starting position which is inner landmark. for index finger    
                #if finger folded changing color to green(As given in specific task3)







                #checking if all fingers are folded(As given in Specific task 5 & 6)





            mp_draw.draw_landmarks(img, hand_landmark,
            mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec((0,0,255),2,2),
            mp_draw.DrawingSpec((0,255,0),4,2))
    

    cv2.imshow("hand tracking", img)
    cv2.waitKey(1)

