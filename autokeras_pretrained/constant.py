from collections import namedtuple

GoogleDriveFile = namedtuple('GoogleDriveFile', ['google_drive_id', 'local_name'])


class Constant:

    # Text Classifier

    BERT_TRAINER_EPOCHS = 4
    BERT_TRAINER_BATCH_SIZE = 32

    # text preprocessor

    EMBEDDING_DIM = 100
    MAX_SEQUENCE_LENGTH = 400
    MAX_NB_WORDS = 5000
    EXTRACT_PATH = "glove/"
    STORE_PATH = ''

    # Download file name

    FILE_PATH = "glove.zip"
    PRE_TRAIN_FILE_LINK = "http://nlp.stanford.edu/data/glove.6B.zip"
    PRE_TRAIN_FILE_NAME = "glove.6B.100d.txt"

    PRE_TRAIN_DETECTION_FILE_LINK = "https://s3.amazonaws.com/amdegroot-models/ssd300_mAP_77.43_v2.pth"

    VOICE_GENERATOR_MODELS = [
        GoogleDriveFile(google_drive_id='1E-B92LZz4dgg8DU81D6pyhOzM9yvvBTj', local_name='vg.pth')]
    VOICE_RECONGINIZER_MODELS = [
        GoogleDriveFile(google_drive_id='1RQQB-Yd-aqb6scWtnu1K4nlSTxTyaKjI', local_name='vr.pth')]
    FACE_DETECTOR_MODELS = [
        GoogleDriveFile(google_drive_id='1QJWKpAHRrAjrYPl6hQNDaoyBjoa_LRgz', local_name='pnet.pt'),
        GoogleDriveFile(google_drive_id='10aCiR393E6TLkp9KPPl4JhZamYqUVBO1', local_name='rnet.pt'),
        GoogleDriveFile(google_drive_id='1RRBtPlzw46peS-A8pyYGsPRHHFIUrSVV', local_name='onet.pt')]
    OBJECT_DETECTOR_MODELS = [
        GoogleDriveFile(google_drive_id='1QGG1trfj-z5_2OGNoSarUB4wx81cG-sa', local_name='oo.pth')]
    SENTIMENT_ANALYSIS_MODELS = [
        GoogleDriveFile(google_drive_id='1flRlQjfIa2toQ6HNmInhqrh4NuxGh8pT', local_name='sa.pth')]
    TOPIC_CLASSIFIER_MODELS = [
        GoogleDriveFile(google_drive_id='1U7C3xPid1ZvBKpkfW9KikrmNui0yJqnk', local_name='tc.pth')]
    PRETRAINED_VOCAB_BERT_BASE_UNCASED = \
        GoogleDriveFile(google_drive_id='1hlPkUSPeT5ZQBYZ1Z734BbnHIvpx2ZLj', local_name='vbbu.txt')
    PRETRAINED_VOCAB_BERT_BASE_CASED = \
        GoogleDriveFile(google_drive_id='1FLytUhOIF0mTfA4A9MtE3aQ1kJr96oTR', local_name='vbbc.txt')
    PRETRAINED_MODEL_BERT_BASE_UNCASED = \
        GoogleDriveFile(google_drive_id='1rp1rVBoQwqgvg-JE8JwLL-adgLE07oTG', local_name='mbbu.pth')
    PRETRAINED_MODEL_BERT_BASE_CASED = \
        GoogleDriveFile(google_drive_id='1YKoGj-e4zoyTabt5dYpgEPe-PAmjOTDV', local_name='mbbc.pth')

    VOICE_RECONGINIZER_LABELS = "_'ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    VOICE_RECONGINIZER_AUDIO_CONF = {'sample_rate': 16000, 'window_size': 0.02, 'window_stride': 0.01,
                                     'window': 'hamming', 'noise_dir': None, 'noise_prob': 0.4,
                                     'noise_levels': (0.0, 0.5)}

    # Image Resize

    MAX_IMAGE_SIZE = 128 * 128

    # SYS Constant

    SYS_LINUX = 'linux'
    SYS_WINDOWS = 'windows'
    SYS_GOOGLE_COLAB = 'goog_colab'

    # Google drive downloader
    CHUNK_SIZE = 32768
    DOWNLOAD_URL = "https://docs.google.com/uc?export=download"
