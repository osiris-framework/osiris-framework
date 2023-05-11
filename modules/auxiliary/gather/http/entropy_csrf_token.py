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


