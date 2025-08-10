from somad import Somad
from personas import Personas
import random

class MarkdownPersona(Somad):  
    def __init__(self) -> None:
        super().__init__()
        task = """You are a Markdown formatter.
Your task is to take the provided plain-text forum post and reformat it using valid CommonMark Markdown syntax without adding or removing any text.

Rules:
* Include all text exactly as provided -- do not paraphrase, summarize, or omit anything.
* Reformat only -- fix spacing, punctuation alignment, and apply Markdown formatting where appropriate.
* Preserve the full content, even if it looks like metadata, tags, or markup.
* Apply formatting intelligently:
   - Use fenced code blocks for code snippets and specify the language if obvious.
   - Use # headings for section titles.
   - Format lists correctly (- or 1. with consistent spacing).
   - Use **bold**, *italic*, and inline code `like this` where appropriate.
   - Preserve blank lines between paragraphs.
* When you need a hard line break in plain text, end the line with a single backslash `\\`. Do not add a backslash:
   - Inside code blocks
   - After headings
   - At the end of list items
   - Anywhere it would change valid Markdown structure
* Every time you would normally insert a hard line break, you must end the line with a single backslash character (\\).  Do not use two spaces or <br>.
* Do not add commentary, explanations, or instructions -- output only the fully formatted Markdown.

Output:
- A single block of Markdown text representing the reformatted post.
- No extra headers, separators, or descriptions.
"""
        self.messages = [
            {
                "role": "system",
                "content": task
            }
        ]
        self.model = "qwen/qwen-2.5-72b-instruct:free"
        self.temperature = 0.5
        self.top_p = 0.7