
import os

TEST_TEMP_AUTO_KERAS_DIR = 'tests/resources/temp/autokeras'
TEST_TEMP_DIR = 'tests/resources/temp'


def clean_dir(path):
    for f in os.listdir(path):
        full_path = os.path.join(path, f)
        if f != '.gitkeep':
            if os.path.isfile(full_path):
                os.remove(full_path)
            else:
                os.rmdir(full_path)
# def mock_nvidia_smi_output(*arg, **kwargs):
#     return \
#         '    Free                        : 1 MiB \n' \
#         '    Free                        : 11176 MiB \n' \
#         '    Free                        : 1 MiB \n' \
#         '    Free                        : 1 MiB'
