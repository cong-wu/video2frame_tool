import cv2
import os


input_dir = '/home/wu/input'
output_dir = '/home/wu/output'

resize_height = 224
resize_width = 224

print('Please wait! Processing Begins.')

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

for file in os.listdir(input_dir):
    file_path = os.path.join(input_dir, file)
    video_files = [name for name in os.listdir(file_path)]

    data_dir = os.path.join(output_dir, file)

    if not os.path.exists(data_dir):
        os.mkdir(data_dir)

    for video in video_files:
        video_filename = video.split('.')[0]
        if not os.path.exists(os.path.join(data_dir, video_filename)):
            os.mkdir(os.path.join(data_dir, video_filename))

        capture = cv2.VideoCapture(os.path.join(input_dir, file, video))
        frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

        extraction_interval = 5
        while frame_count // extraction_interval < 16:
            extraction_interval -= 1

        count = 0
        success = True
        i = 0

        while count < frame_count and success:
            success, frame = capture.read()
            if frame is None:
                continue
            if count % extraction_interval == 0:
                if (frame_width != resize_width) or (frame_height != resize_height):
                    frame = cv2.resize(frame, (resize_width, resize_height))
                cv2.imwrite(filename=os.path.join(data_dir, video_filename, '000{}.jpg'.format(str(i))), img=frame)
                i += 1
            count += 1
        capture.release()

print('Congratulations! Processing Ends.')
