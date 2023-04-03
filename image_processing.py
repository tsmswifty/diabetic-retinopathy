import os
import cv2
import multiprocessing

import numpy as np


def crop_image1(img, tol=7):
    # img is image data
    # tol  is tolerance

    mask = img > tol
    return img[np.ix_(mask.any(1), mask.any(0))]


def crop_image_from_gray(img, tol=7):
    if img.ndim == 2:
        mask = img > tol
        return img[np.ix_(mask.any(1), mask.any(0))]
    elif img.ndim == 3:
        gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        mask = gray_img > tol

        check_shape = img[:, :, 0][np.ix_(mask.any(1), mask.any(0))].shape[0]
        if check_shape == 0:  # image is too dark so that we crop out everything,
            return img  # return original image
        else:
            img1 = img[:, :, 0][np.ix_(mask.any(1), mask.any(0))]
            img2 = img[:, :, 1][np.ix_(mask.any(1), mask.any(0))]
            img3 = img[:, :, 2][np.ix_(mask.any(1), mask.any(0))]
            #         print(img1.shape,img2.shape,img3.shape)
            img = np.stack([img1, img2, img3], axis=-1)
        #         print(img.shape)
        return img


def circle_crop(img, sigmaX=10):
    """
    Create circular crop around image centre
    """

    img = cv2.imread(img)
    img = crop_image_from_gray(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    height, width, depth = img.shape

    x = int(width / 2)
    y = int(height / 2)
    r = np.amin((x, y))

    circle_img = np.zeros((height, width), np.uint8)
    cv2.circle(circle_img, (x, y), int(r), 1, thickness=-1)
    img = cv2.bitwise_and(img, img, mask=circle_img)
    img = crop_image_from_gray(img)
    img = cv2.addWeighted(img, 4, cv2.GaussianBlur(img, (0, 0), sigmaX), -4, 128)
    return img


def circle_crop_wrapper(dir_arg):
    for file in os.listdir(dir_arg):
        print(file)
        img = circle_crop(os.path.join(dir_arg, file))
        cv2.imwrite(os.path.join(dir_arg + "_processed", file), img)


def process_image(dir_arg):
    for file in os.listdir(dir_arg):
        print(file)
        # read image
        image = cv2.imread(os.path.join(dir_arg, file))
        scale_percent = 30
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

        # crop ROI using otsu
        # https://stackoverflow.com/questions/28759253/how-to-crop-the-internal-area-of-a-contour
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]
        cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
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

        cv2.imwrite(os.path.join(dir_arg + "_processed", file), image)


if __name__ == "__main__":
    # processes = [
    #     multiprocessing.Process(target=process_image, args=(str(dir_arg),))
    #     for dir_arg in range(5)
    # ]
    # [p.start() for p in processes]
    # result = [p.join() for p in processes]
    # print(result)
    circle_crop_wrapper("test_imgs")
