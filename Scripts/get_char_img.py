"""
指定したRGBカラー範囲内の画素を黒色にする。範囲外の画素を白色にする。
"""
import cv2


def get_char_img(img_path: str, \
    rgb_min_max_list: list = [ \
        216, 255, \
        216, 255, \
        216, 255]):
    """
    Load an image, and convert pixels within a specified RGB range to black, 
    while converting others to white.

    Args:
        img_path (str): The file path to the image.
        rgb_min_max_list (list, optional): 
            A list containing minimum and maximum 
            values for each of the RGB channels 
            [r_min, r_max, g_min, g_max, b_min, b_max]. 
            Defaults to [216, 255, 216, 255, 216, 255].

    Returns:
        np.ndarray: 
            The processed image with pixels in the specified RGB range set 
            to black and others set to white.
    """
    # Load image
    img = cv2.imread(img_path)
    # Extract RGB min-max-values
    r_min, r_max, g_min, g_max, b_min, b_max = rgb_min_max_list
    # Operate all pixels
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            b, g, r = img[y, x]
            # Check RGB range between min and max
            if b_min <= b <= b_max \
                and g_min <= g <= g_max \
                and r_min <= r <= r_max:
                # to black
                img[y, x] = [0, 0, 0]
            else:
                # to white
                img[y, x] = [255, 255, 255]
    return img


def save_to_char_img(img_path: str, save_path: str, \
    rgb_min_max_list: list = [ \
        216, 255, \
        216, 255, \
        216, 255]) -> str:
    """
    Process an image to convert pixels within a specified RGB range to black 
    and others to white, then save the processed image to a specified path.

    Args:
        img_path (str): The file path to the input image.
        save_path (str): The file path to save the processed image.
        rgb_min_max_list (list, optional): 
            A list containing minimum and maximum 
            values for each of the RGB channels 
            [r_min, r_max, g_min, g_max, b_min, b_max]. 
            Defaults to [216, 255, 216, 255, 216, 255].

    Returns:
        str: A confirmation message indicating that the processed image has been saved.
    """
    # Load image with specified RGB range to black, while converting others to white
    img = get_char_img(img_path, rgb_min_max_list = rgb_min_max_list)
    # Save char-img
    cv2.imwrite(save_path, img)
    # Return a confirmation message
    return "char img saved"
