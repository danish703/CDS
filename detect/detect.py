import cv2
from django.conf import settings
detector = cv2.AKAZE_create()
import os
AKAZE = cv2.DescriptorMatcher_create(cv2.DescriptorMatcher_BRUTEFORCE_HAMMING)

train_url = settings.BASE_DIR
print(train_url)
TrainingImageArray = ["F:/CDS/detect/dataset/1.jpg",
                      "F:/CDS/detect/dataset/2.jpg",
                      "F:/CDS/detect/dataset/5.jpg",
                      "F:/CDS/detect/dataset/5r.jpg",
                      "F:/CDS/detect/dataset/10.jpg",
                      "F:/CDS/detect/dataset/20.jpg",
                      "F:/CDS/detect/dataset/50.jpg",
                      "F:/CDS/detect/dataset/100.jpg",
                      "F:/CDS/detect/dataset/500.jpg",
                      "F:/CDS/detect/dataset/1000.jpg"
                      ]
#
# TrainingImageArray = [ os.path.join(train_url,'1.jpg'),
#                        os.path.join(train_url, '2.jpg'),
#                        os.path.join(train_url, '5.jpg'),
#                        os.path.join(train_url, '5r.jpg'),
#                        os.path.join(train_url, '10.jpg'),
#                        os.path.join(train_url, '20.jpg'),
#                        os.path.join(train_url, '50.jpg'),
#                        os.path.join(train_url, '100.jpg'),
#                        os.path.join(train_url, '500.jpg'),
#                        os.path.join(train_url,'1000.jpg'),]

elements = ["1", "2",
            "5", "5",
            "10", "20",
            "50", "100",
            "500", "1000",
            ]

accuracy_ratio = 0.9

DesArray = []
for i in range(len(TrainingImageArray)):
    getting_image_array = TrainingImageArray[i]
    reading_image_array = cv2.imread(getting_image_array, 0)
    trainKP, trainDesc = detector.detectAndCompute(reading_image_array, None)
    DesArray.append(trainDesc)


def detechImage(imageSource):
    userimage = cv2.imread(imageSource, 0)
    QueryKP, QueryDesc = detector.detectAndCompute(userimage, None)

    maximum_point = 0
    index_element = 0
    for i in range(len(TrainingImageArray)):
        matches = AKAZE.knnMatch(QueryDesc, DesArray[i], k=2)

        # print("DETECTING - " + elements[i])

        match = 0
        for m, n in matches:
            if (m.distance < accuracy_ratio * n.distance):
                match += 1
        # print(match)

        if match > maximum_point:
            maximum_point = match
            index_element = i
    return elements[index_element]
