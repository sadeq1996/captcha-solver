from easyocr import Reader
class Captcha:
    
    def __init__(self,Image):
        self.Image = Image
        
    def captchaDetctor(self):
        reader = Reader(['en'])
        results = reader.readtext(self.Image,detail=0)

        print(results)

x= Captcha("2_c.jpg")
print(x.captchaDetctor())