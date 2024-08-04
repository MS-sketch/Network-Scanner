import re

def convert_text_to_html(input_text):

    # Simple text-based conversion
    html_content = convert_markdown_to_html(input_text)

    return html_content

def convert_markdown_to_html(text):
    # Convert markdown-like formatting to HTML

    # Convert "## " to <h2> with two line breaks after it
    text = re.sub(r'## (.*)', r'<h2>\1</h2>', text)

    # Convert "**" to <strong> with one line break after it
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong><br>', text)

    # Convert each point or paragraph to a new line
    text = re.sub(r'\n', r'<br>', text)

    # Ensure the text is inside <p> tags
    text = f"<p>{text}</p>"

    return text