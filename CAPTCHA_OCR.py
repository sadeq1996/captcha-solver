from easyocr import Reader
class Captcha:
     
    @staticmethod
    def captchaDetctor(Image):
        reader = Reader(['en'])
        results = reader.readtext(Image, detail=0)

        print(results)

def Run():
    Captcha.captchaDetctor("1_c.jpg")

if __name__ == "__main__":
    Run()
    