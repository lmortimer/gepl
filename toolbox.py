# chatgpt generated this
def extract_text(text: str, start_marker: str, end_marker: str) -> str:
    start_index = text.find(start_marker) + len(start_marker)
    end_index = text.find(end_marker, start_index)
    return text[start_index:end_index]


# chatgpt generated this
def is_valid_python_syntax(string):
    try:
        compile(string, '<string>', 'exec')
        return True
    except SyntaxError:
        return False
