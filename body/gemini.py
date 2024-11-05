import google.generativeai as genai
import re
def gemini(data):
    prompt = f""" 
        {data}
    The above string is a job description. I want to extract technical keywords and organize them into a Python dictionary. For example, keywords like Frontend, Backend, SQL, etc. Each key will have a list of values related to it. If a key has no values, it should not be added. Only provide the Python dictionary, without any extra analysis.   note dont leave any points this dictionary is going to pass the ats
    """
    genai.configure(api_key="AIzaSyB4XgWlQ6WOlMjcYnpw6uzFPgm9ug2qwM0")
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    input_string = f"""{response.text}"""

    matches = re.findall(r'\{\s*([^}]*)\s*\}', input_string)

    cleaned_matches = [match.strip() for match in matches]

    add = ''

    for match in cleaned_matches:
        add += match

    return (f"{{ {add} }}")
