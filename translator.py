def translate_payload(request_dict):
    summary = payload_dict.get('summary')
    title = payload_dict.get('title')
    web_url = payload_dict.get('web_url')
    display_name = payload_dict.get('display_name')
    text = '<{web_url}|{display_name}> - {title}'
    text = text.format(title=title, web_url=web_url, display_name=display_name)
    if len(summary) > 0:
        text = '{}\n{}'.format(text, summary)
    payload = {'text': text}
    return payload
