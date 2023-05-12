import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

APIKEY="zNTkM7s5ZFjfHdmPbgz_aiVLBr_DnrNbIknD6IitwrZ8"
URL="https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/2b274465-b98f-4d46-87db-957a0b01343f" 
authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
version='2018-05-01',
authenticator=authenticator)
language_translator.set_service_url(URL)

def english_to_french(english_text: str):
    """Function takes the string in englsh and return translated string in french"""
    try:
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        #Getting the pure translation string
        french_text = translation['translations'][0]['translation']
        return french_text
    except Exception as error:
        print(error)
        return None


def french_to_english(french_text: str):
    """Function takes the string in french and return translated string in english"""
    try:
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        #Getting the pure translation string
        english_text = translation['translations'][0]['translation']
        return english_text
    except Exception as error:
        print(error)
        return None