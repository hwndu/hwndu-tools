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
        parsed['thumbnail'] = item['thumbnail_url']
        parsed['streamed_at'] = item['streamed_at']
        if 'secure_progessive_url_hd' in item:
            parsed['url'] = item['secure_progressive_url_hd']
        elif 'progressive_url_hd' in item:
            parsed['url'] = item['progressive_url_hd']
        else:
            continue
        parsed_list.append(parsed)
    database = {'store': parsed_list}

    sfile = file("database.json")
    existing_database = json.load(sfile)
    sfile.close()
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

    dfile = file("database.json", 'w')
    dfile.write(json.dumps(existing_database))
    dfile.close()

if __name__ == "__main__":
    main()
