import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()
api_key="zNTkM7s5ZFjfHdmPbgz_aiVLBr_DnrNbIknD6IitwrZ8"
url="https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/2b274465-b98f-4d46-87db-957a0b01343f" 


authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url(url)

def english_to_french(english_text):

    try:
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        french_text = translation['translations'][0]['translation']
    except:
        french_text = None

    return french_text

def french_to_english(french_text):

    try:
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        english_text = translation['translations'][0]['translation']
    except:
        english_text = None
    return english_text
