import openai
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

# Function to generate code using OpenAI
def generate_code(prompt, language):
    response = openai.Completion.create(
        model="text-davinci-003",  # or GPT-4 if available
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    code = response.choices[0].text.strip()
    return code

# Function to add syntax highlighting
def highlight_code(code, language):
    lexer = get_lexer_by_name(language.lower())
    formatter = HtmlFormatter(full=True)
    highlighted_code = highlight(code, lexer, formatter)
    return highlighted_code
