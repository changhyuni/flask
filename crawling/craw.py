  
import urllib.request as req
image_url = 'http://cafefiles.naver.net/20111015_243/style0488_131866632399251ywj_jpg/%BE%C6%B1%E2%B0%ED%BE%E7%C0%CC1_style0488.jpg'
html_url = 'https://www.google.com/'


image_dir = '/home/student/python_image/test1.jpg'
html_dir = '/home/student/python_html/index.html'

try:
    file1, header1 = req.urlretrieve(image_url, image_dir)
    file2, header2 = req.urlretrieve(html_url, html_dir)
except Exception as e:
    print("다운로드 실패")
    print(e)
else:
    print(header1)
    print(header2)


    print(F"filename1 : {file1}.")
    print("filename2 {}".format(file2))
    
    print("성공입니다 !")
