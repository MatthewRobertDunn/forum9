from typing import List
from open_router_models import FastModels
from somad import Somad


class MarkdownPersona(Somad):
    @property
    def model_bias_exponent(self) -> float:
        return 3.0

    @property
    def models(self) -> List[str]:
        # Base list of models — subclasses can override this
        return FastModels
    def __init__(self) -> None:
        super().__init__()
        task = """You are a Markdown formatter.
Your task is to take the provided plain-text forum post and reformat it using valid CommonMark Markdown syntax without adding or removing any text.

Rules:
* Include all text provided -- do not paraphrase, summarize, or omit anything.
* Apply formatting intelligently:
   - Use fenced code blocks for code snippets and specify the language if obvious.
   - Use # headings for section titles.
   - Format lists correctly (- or 1. with consistent spacing).
   - Use **bold**, *italic*, and inline code `like this` where appropriate.
   - Preserve blank lines between paragraphs.
   - Preserve hard line breaks in the original plain text where appropriate.
   - When you need a hard line break in the output, end the line with two spaces not <br> or \\
* Do not add additional content such as new headers to the document, only adjust the style, formatting, wordwrapping, whitespace, etc.
* Do not add commentary, explanations, or instructions -- output only the fully formatted Markdown.

Output:
- The Markdown text representing the reformatted plain text post.
- No extra headers, separators, explanations, or meta-data.
"""
        self.messages = [
            {
                "role": "system",
                "content": task
            }
        ]
        self.temperature = 0.5
        self.top_p = 0.7
