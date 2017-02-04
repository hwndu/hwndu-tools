import json
import requests

stream_url = "https://api.new.livestream.com/accounts/23093026/events/6897778/"

def get_manifest():
    r = requests.get(stream_url)
    return r.content

def main():
    manifest = json.loads(get_manifest())
    feeds = manifest['feed']['data']
    parsed_list = []
    for i in feeds:
        item = i['data']
        parsed = {}
        parsed['id'] = item['asset_id']
        parsed['original_duration'] = item['original_duration']
        parsed['url'] = item['secure_progressive_url_hd']
        parsed['streamed_at'] = item['streamed_at']
        parsed['thumbnail'] = item['thumbnail_url']
        parsed_list.append(parsed)
    database = {'store': parsed_list}

    existing_database = json.load(file("database.json"))
    existing_id_list = []
    for i in existing_database['store']:
        existing_id_list.append(i['id'])

    new_list = []
    for i in parsed_list:
        if i['id'] not in existing_id_list:
            new_list.append(i)
            existing_database['store'].append(i)

    for i in new_list:
        print "%s %s %s" % (i['id'], i['url'], i['thumbnail'])

    file("database.json", 'w').write(json.dumps(existing_database))

if __name__ == "__main__":
    main()
