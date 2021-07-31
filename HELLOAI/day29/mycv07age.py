from flask import Flask,render_template, jsonify, request 
import requests, random, json
from bs4 import BeautifulSoup

app = Flask(__name__, static_url_path="", static_folder="static")

@app.route("/") #url-mapping
@app.route("/kakao_v2") #url-mapping
def kakao_v2():
    return render_template('kakao_v2.html')

@app.route("/pic_check2", methods=['POST'])
def kakao_pic2():
    image_url = request.form["text"]
    
    API_URL = 'https://dapi.kakao.com/v2/vision/face/detect'
    MYAPP_KEY = '2b712cb6a2c570831e118a005bd718fe'
    
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}
    data = { 'image_url' : image_url}
    resp = requests.post(API_URL, headers=headers, data=data)
    
    resp.raise_for_status()
    print(resp)
    print(type(resp))
    
    result = json.loads(resp.text)
    
    male ="%10f" %  result['result']['faces'][0]['facial_attributes']['gender']['male']
    female ="%10f" %  result['result']['faces'][0]['facial_attributes']['gender']['female']
    age = int(result['result']['faces'][0]['facial_attributes']['age'])
    
    print(male)
    print(female)
    print(age)
    
    sex =""
    if male > female:
        sex = "남자"
    else:
        sex = "여자"
    
    #연령대
    age_group = int(age/10)*10
    print(age_group)
     
    #크롤링한 이미지 태그들 
    img_tags = search_soup(age_group, sex)
    
    face_info = {"male":male, "female":female, "age":age, "sex":sex, "age_group":age_group ,"img_tags":img_tags}
    return jsonify(face_info)
 
    
        
if __name__ == "__main__":
    app.run(debug=True)
#   app.run(host='localhost', port=5000)


