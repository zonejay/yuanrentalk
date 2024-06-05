import cv2
import pytesseract
import base64
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
import hashlib

def get_hidden_class(data):
    # 输入字符串
    input_str = data["key"] + data["value"]
    hidden = hashlib.md5(base64.b64encode(input_str.encode()).decode().replace('=', '').encode()).digest().hex()
    return hidden

# 解码Base64图像数据为OpenCV图像
def base64_to_cv2(base64_data):
    image_data = base64.b64decode(base64_data)
    np_array = np.frombuffer(image_data, np.uint8)
    cv2_image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
    return img_rgb

# 识别数字
def recognize_digit(cv2_image):
    custom_config = r'--tessdata-dir /usr/share/tesseract-ocr/4.00/tessdata/ --oem 3 --psm 10 digits'
    text = pytesseract.image_to_string(cv2_image, lang="eng", config=custom_config)
    return text.strip()

def get_number(numbers):
    # 按照 numbers中元素在数组中的位置减去offset计算新的offset来生成数组
    for i, number in enumerate(numbers):
        number["offset"] = number["offset"] + i
    
    # 按照offset排序
    sorted_numbers = sorted(numbers, key=lambda x: x["offset"])

    # 拼接数字
    concatenated_number = int("".join(str(item["number"]) for item in sorted_numbers))
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
            if 'class' in img_tag.attrs and hidden_class in img_tag['class']:
                continue  # 如果父元素包含"display: none"样式，则跳过该图像
            style = img_tag['style']
            left_px = float(re.search(r'left:\s*(-?\d+\.?\d*)px', style).group(1))
            visible_images.append(left_px)
            base64_data = img_tag['src'].split(',')[1]
            cv2_image = base64_to_cv2(base64_data)
            number = recognize_digit(cv2_image)
            print(number)
            if number.isdigit():
                # offset等于left_px除以11.5再取整
                offset = int(left_px / 11.5)
                numbers.append({"number": number, "left_px": left_px, "offset": offset})
        # print(numbers)
        # 控制台输出分割线
        print("-" * 50)
        number = get_number(numbers)
        print(number)
        print("-" * 50)
        total += number
    print(total)
    return total
    # 46030681

def test(number = 6, count = 100):
    # 读取项目目录下assets/digits下面的6.png
    image = cv2.imread(f'assets/digits/{number}.png')
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # 识别100次数字并统计正确结果
    correct_count = 0
    for _ in range(count):
        recognized_number = recognize_digit(img_rgb)
        print(recognized_number)
        if recognized_number == f'{number}':
            correct_count += 1
    print(correct_count)  # 输出识别的数字
    
def main():
    # 请求前5页数据并计算累计和
    total = 0
    for page in range(1, 6):
        response = requests.get(f'https://match.yuanrenxue.cn/api/match/4?page={page}')
        data = response.json()
        total += get_all_visible_iamge(data["info"], get_hidden_class(data))
    
    # 输出累计和 226449
    print(f"total {total}")

if __name__ == "__main__":
    main()
    # test(5, 1)