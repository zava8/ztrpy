import asyncio
from googletrans import Translator
from u_to_i import u_to_i
# https://pypi.org/project/googletrans/
# stable api https://cloud.google.com/translate/docs
# translator = Translator()
# gugl_sheet https://stackoverflow.com/questions/60824929/translate-an-entire-google-sheet-using-google-translate

async def translate_text(text):
    async with Translator() as translator:
        result = await translator.translate(text, dest='hi')
        print(result)
        return result
if __name__ == "__main__":
    text = "Hello, world!"
    translated = asyncio.run(translate_text(text))
    ioz = {"i": translated.text, "o": ""}
    u_to_i(ioz)
    print(ioz['o'])