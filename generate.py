import os
from typing import List
from dotenv import load_dotenv

from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    BaseMessage
)

from datatypes import CodeAndDescriptionResponse
from prompts import STARTUP_PROMPT, create_generate_code_prompt
from toolbox import extract_text, is_valid_python_syntax

load_dotenv()

chat = ChatOpenAI(temperature=0, openai_api_key=os.environ["OPENAI_KEY"])

chain = LLMChain(llm=chat, prompt=STARTUP_PROMPT)


def generate_code_with_context(message: str, context: List[BaseMessage]) -> CodeAndDescriptionResponse:

    result = chain.run(context + create_generate_code_prompt(message=message))

    # print('RAW debug: ' + result)

    possibly_code = extract_text(result, "STARTCODE", "ENDCODE").strip()
    description = extract_text(result, "STARTDESC", "ENDDESC").strip()

    if is_valid_python_syntax(possibly_code):
        code = possibly_code
    else:
        code = ""

    return CodeAndDescriptionResponse(code=code, description=description)
