import asyncio
import requests
import pytesseract
import signal
from core.ModuleObtainer import obtainer
from utilities.Colors import color
from utilities.Messages import print_message
from utilities.Tools import tools
from PIL import Image

info = {
    'author': 'Luis Eduardo Jacome Valencia',
    'date': '2022/12/13',
    'rank': 'Excellent',
    'path': 'auxiliary/gather/http/captcha_solver.py',
    'category': 'auxiliary',
    'license': 'GPL-2.0',
    'description': 'Solve weak captcha and send the response to an endpoint. This is a version 1 and does not have still all the cases.',
    'references': ['']
}
options = {
    'rhost': ['Yes', 'Set target to attack', ''],
    'rport': ['No', 'Set port to attack: i.e :8080', ''],
    'webpath': ['Yes', 'Set uri where is the image of captcha', '/'],
    'psm': ['Yes', 'That affects how Tesseract splits image in lines of text and words', '10'],
    'oem': ['Yes', 'Tesseract has several engine modes with different performance and speed', '3'],
    'quantity_requests': ['No', 'Set how many requests do you want to try', '10'],
    'response_endpoint': ['Yes', 'Set webpath where the solved captcha should be sent. i.e www.example.com/?captcha_code=', '/'],

    'results': ['No', 'Save data in a folder', tools.temp_dir()['message'] + '/']
}

required = {
    'start_required': 'True',
    'check_required': 'False'
}


class CaptchaSolver():
    def __init__(self, _complete_url, _response_endpoint,  _psm, _oem,  _results):
        self.complete_url = _complete_url
        self.response_endpoint = _response_endpoint
        self.psm = _psm
        self.oem = _oem
        self.results = _results

    def __call__(self):
        asyncio.run(self.main())

    async def ocr_image_from_url(self):
        try:

            # Send a GET request to the URL to download the image
            response = requests.get(self.complete_url)

            # Save the image to a temporary file
            with open(self.results + "temp.png", "wb") as f:
                f.write(response.content)

            # Open the image
            image = Image.open(self.results + "temp.png")

            # Use Tesseract to extract the text from the image
            # Set some parameters to improve the accuracy of the OCR
            text = pytesseract.image_to_string(image, lang="eng", config="--psm " + self.psm + "--oem " + self.oem)

            print(color.color("blue", "[*] Text converted ->  " + text))
            print(color.color("green", "[*] Sending the text converted to the endpoint"))

            print(requests.get(self.response_endpoint + text).status_code)
        except:
            pass

    async def main(self):
        # Extract the text from the image

        text = await self.ocr_image_from_url()

        # Print the extracted text
        print(text)


def exploit():
    """ main exploit function """
    try:
        print_message.start_execution()

        _rhost = obtainer.options['rhost'][2]
        _rport = obtainer.options['rport'][2]
        _webpath = obtainer.options['webpath'][2]
        _response_endpoint = obtainer.options['response_endpoint'][2]
        _psm = obtainer.options['psm'][2]
        _oem = obtainer.options['oem'][2]
        _how_many_requests = obtainer.options['quantity_requests'][2]
        _results = obtainer.options['results'][2]

        _complete_url = _rhost + _rport + _webpath

        for i in range(0, int(_how_many_requests)):
            try:
                captcha_solver = CaptchaSolver(_complete_url, _response_endpoint, _psm, _oem, _results)
                captcha_solver()
                signal.signal(signal.SIGINT, captcha_solver)

            except KeyboardInterrupt:
                break

    except (AttributeError, TypeError) as e:
        print_message.execution_error("lgray", " You must enter the parameters!")
        return False

    print_message.end_execution()


