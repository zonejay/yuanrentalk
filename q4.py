import cv2
import pytesseract
from PIL import Image
import base64
from io import BytesIO
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
import hashlib

def get_hidden_class(data):
    # 输入字符串
    input_str = data["key"] + data["value"]
    hidden = hashlib.md5(base64.b64encode(input_str.encode()).decode().replace('=', '').encode()).digest().hex()
    print(hidden)

# 解码Base64图像数据为OpenCV图像
def base64_to_cv2(base64_data):
    image_data = base64.b64decode(base64_data)
    np_array = np.frombuffer(image_data, np.uint8)
    cv2_image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    return cv2_image

# 识别数字
def recognize_digit(cv2_image):
    gray = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    custom_config = r'--oem 3 --psm 10 digits'
    text = pytesseract.image_to_string(thresh, config=custom_config)
    return text.strip()

def get_number(numbers):
    # 按照 left_px 属性从小到大排序
    sorted_numbers = sorted(numbers, key=lambda x: x["left_px"])

    # 拼接数字
    concatenated_number = int("".join(str(item["number"]) for item in sorted_numbers))
    print(concatenated_number)
    return concatenated_number

def get_all_visible_iamge(html, hidden_class):
    # 使用Beautiful Soup解析HTML
    soup = BeautifulSoup(html, 'html.parser')

    # 获取所有显示的图像
    visible_images = []
    total = 0
    for image_container in soup.find_all('td'):
        numbers = []
        for img_tag in image_container.find_all('img'):
            print(img_tag['class'])
            if 'class' in img_tag.attrs and hidden_class in img_tag['class']:
                print('this tag is hidden')
                continue  # 如果父元素包含"display: none"样式，则跳过该图像
            style = img_tag['style']
            left_px = float(re.search(r'left:\s*(-?\d+\.?\d*)px', style).group(1))
            visible_images.append(left_px)
            base64_data = img_tag['src'].split(',')[1]
            cv2_image = base64_to_cv2(base64_data)
            number = recognize_digit(cv2_image)
            if number.isdigit():
                numbers.append({"number": number, "left_px": left_px})
        number = get_number(numbers)
        total += number
    print(total)
    # 46030681

if __name__ == "__main__":
    # 发送请求获取样式和图像数据
    response = requests.get('https://match.yuanrenxue.cn/api/match/4?page=1')
    data = response.json()
    print(data['key'], data['value'])
    get_all_visible_iamge(data["info"], get_hidden_class(data))