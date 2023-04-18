from generate import generate_code_with_context
from prompts import create_generated_code_executed_prompt, create_user_executed_code_prompt

import colorama

GENERATE_PREFIX = "`"

context = []

while True:
    try:
        input_str = input(">> ")

        # dump the context for debugging
        if input_str == "!":
            print(context)
            output = ""

        # prompt the LLM and execute the code
        elif input_str.startswith(GENERATE_PREFIX):
            generate_result = generate_code_with_context(message=input_str[1::], context=context)
            print(colorama.Fore.BLUE + "Desc: " + generate_result.description + colorama.Style.RESET_ALL)
            print(colorama.Fore.CYAN + "Code: " + generate_result.code + colorama.Style.RESET_ALL)

            output = exec(generate_result.code)

            context = context + create_generated_code_executed_prompt(message=input_str, code=generate_result.code, result=output)

        # the user entered python, execute it
        else:
            output = exec(input_str)

            context = context + create_user_executed_code_prompt(code=input_str, result=output)

        if str(output) != "None":
            print(output)

    except Exception as e:
        print("Error:", e)
