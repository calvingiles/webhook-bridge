def translate_payload(payload_dict):
    summary = payload_dict.get('summary')
    title = payload_dict.get('title')
    web_url = payload_dict.get('web_url')
    display_name = payload_dict.get('creator', {}).get('display_name')
    text = '<{web_url}|{title}> - submitted by {display_name}'
    text = text.format(title=title, web_url=web_url, display_name=display_name)
    if len(summary) > 0:
        summary = summary.replace('</p><p>', '\n')
        summary = summary.replace('<p>', '')
        summary = summary.replace('</p>', '')
        summary = summary.replace('<br />', '\n')
        summary = summary.replace('<strong>', '*')
        summary = summary.replace('</strong>', '*')
        summary = summary.replace('<em>', '_')
        summary = summary.replace('</em>', '_')
        summary = summary.replace('&nbsp;', ' ')

        text = '{}\n{}'.format(text, summary)
    payload = {'text': text}
    return payload
