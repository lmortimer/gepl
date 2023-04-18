from dataclasses import dataclass

# datatypes, because the python interpreter bombs if you call this types.py


@dataclass
class CodeAndDescriptionResponse:
    """
    Stores the code and description parsed out from the LLM response
    """
    code: str
    description: str
