from typing import List
from somad import Somad


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
   - Preserve hard line breaks in the original plain text.
   - When you need a hard line break in the output, end the line with a two spaces  
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
