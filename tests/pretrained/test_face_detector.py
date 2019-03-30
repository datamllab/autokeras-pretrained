from autokeras_pretrained.face_detector import FaceDetector
import os

from tests.common import TEST_TEMP_DIR, clean_dir


def test_face_detector():
    img_file, out_file = 'tests/resources/images_test/face_detector.jpg', os.path.join(TEST_TEMP_DIR, 'output.jpg')
    if os.path.exists(out_file):
        os.remove(out_file)
    face_detection = FaceDetector()
    bboxs1, landmarks1 = face_detection.predict(img_file, out_file)
    assert os.path.exists(out_file)
    bboxs2, landmarks2 = face_detection.predict(img_file)
    assert bboxs1.shape == bboxs2.shape == (11, 5) and landmarks1.shape == landmarks2.shape == (11, 10)
    clean_dir(TEST_TEMP_DIR)
