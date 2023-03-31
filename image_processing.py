import os
import cv2
import multiprocessing


def process_image(dir_arg):
    for file in os.listdir("data_sorted/" + dir_arg):
        # read image
        image = cv2.imread(os.path.join("data_sorted", dir_arg, file))
        scale_percent = 30
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

        # crop ROI using otsu
        # https://stackoverflow.com/questions/28759253/how-to-crop-the-internal-area-of-a-contour
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]
        #
        # # Find contour and sort by contour area
        cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
        #
        # # Find bounding box and extract ROI
        for c in cnts:
            x, y, w, h = cv2.boundingRect(c)
            ROI = image[y : y + h, x : x + w]
            break

        height, width, _ = ROI.shape
        size = min(height, width)
        x = int((width - size) / 2)
        y = int((height - size) / 2)
        crop_img = ROI[y : y + size, x : x + size]

        # CLAHE
        # img = cv2.fastNlMeansDenoisingColored(crop_img, None, 1, 1, 7, 21)
        # img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        # clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        # img_yuv[:, :, 0] = clahe.apply(img_yuv[:, :, 0])
        # img = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

        # apply graham processing https://arxiv.org/pdf/1705.00771.pdf
        image = cv2.addWeighted(
            crop_img, 4, cv2.GaussianBlur(crop_img, (0, 0), 10), -4, 128
        )

        cv2.imwrite(os.path.join("data_processed", dir_arg, file), image)


if __name__ == "__main__":
    processes = [
        multiprocessing.Process(target=process_image, args=(str(dir_arg),))
        for dir_arg in range(5)
    ]
    [p.start() for p in processes]
    result = [p.join() for p in processes]
    print(result)
