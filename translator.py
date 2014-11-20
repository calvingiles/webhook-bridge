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


def translate_docker_to_slack(payload_dict):
    repository = payload_dict.get('repository', {})
    repo_name = repository.get('repo_name', '<repo_name>')
    repo_url = repository.get('repo_url', '<repo_url>')
    push_data = payload_dict.get('push_data', {})
    pusher = push_data.get('pusher', '<pusher>')
    
    text = "[<{repo_url}|{repo_name}>] new image pushed by {pusher}"
    text = text.format(repo_url=repo_url, repo_name=repo_name, pusher=pusher)
    
    payload = {'text': text}
    return payload
