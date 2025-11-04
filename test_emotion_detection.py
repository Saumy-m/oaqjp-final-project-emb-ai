''' Import required libraries for testing file to test the module'''
import unittest
from EmotionDetection import emotion_detection
''' class that tests the function at once'''
class TestEmotionDetection(unittest. TestCase):
    def test_emotion_detector(self):
        # test 1
        self.assertEqual(emotion_detection.emotion_detector("I am glad this happened")["dominant_emotion"],"joy")
        # test 2
        self.assertEqual(emotion_detection.emotion_detector("I am really mad about this")["dominant_emotion"], "anger")
        # test 3
        self.assertEqual(emotion_detection.emotion_detector("I am disgusted just hearing about this")["dominant_emotion"], "disgust")
        # test 4
        self.assertEqual(emotion_detection.emotion_detector("I am sad about this")["dominant_emotion"],"sadness")
        # test 5
        self.assertEqual(emotion_detection.emotion_detector("I am really afraid this will happen")["dominant_emotion"],"fear")

if __name__ == "__main__":
    unittest.main()