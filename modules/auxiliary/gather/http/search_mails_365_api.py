import asyncio
import adal
import requests
from core.ModuleObtainer import obtainer
from utilities.Messages import print_message

info = {
    'author': 'Luis Eduardo Jacome Valencia',
    'date': '2022/12/14',
    'rank': 'Normal',
    'path': 'auxiliary/gather/http/search_mails_365_api.py',
    'category': 'auxiliary',
    'license': 'GPL-2.0',
    'description': 'Search keywords in your emails by O365 API.',
    'references': ['']
}
options = {
    'email': ['Yes', 'Set the user for authentication: user@domain.com', ''],
    'password': ['Yes', 'Set the password', ''],
    'keyword': ['Yes', 'Set the keyword to search', 'Password']
}

required = {
    'start_required': 'True',
    'check_required': 'False'
}


async def authenticate_with_office365(_user_at_domain, _password):
    username = _user_at_domain
    password = _password

    # Create an auth context
    context = adal.AuthenticationContext("https://login.microsoftonline.com/common")

    # Auth thought token
    token = context.acquire_token_with_username_password(
        "https://graph.microsoft.com",
        username,
        password,
        "mi_client_id" # It's not necessary have a client_id
    )

    # Get token
    access_token = token["accessToken"]

    return access_token


# Search the keyword
async def search_emails(access_token, keyword):
    # Create a http client
    client = requests.client()

    # Search mails with keyword and with the token
    response = client.get("https://graph.microsoft.com/v1.0/me/messages",
                          params={
                              "q": keyword
                          },
                          headers={
                              "Authorization": "Bearer " + access_token
                          }
                          )

    # Get the emails
    emails = response.json()["value"]

    for email in emails:
        print(email["subject"])


def exploit():
    """ main exploit function """
    try:
        print_message.start_execution()

        _email = obtainer.options['email'][2]
        _password = obtainer.options['password'][2]
        _keyword = obtainer.options['keyword'][2]

        # Event loop in Asyncio
        loop = asyncio.get_event_loop()

        # Auth in O365
        access_token = loop.run_until_complete(authenticate_with_office365())

        #  Search mails by O365 API
        loop.run_until_complete(search_emails(access_token, _keyword))


    except (AttributeError, TypeError) as e:
        print_message.execution_error("lgray", " You must enter the parameters!")
        return False

    print_message.end_execution()

