import json
import requests
import sys

stream_url = "https://api.new.livestream.com/accounts/23093026/events/6897778/feed.json?type=video&newer=-1&older=1000"

def get_manifest():
    r = requests.get(stream_url)
    return r.content

def main():
    manifest = json.loads(get_manifest())
    feeds = manifest['data']
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
        elif 'secure_progressive_url' in item:
            parsed['url'] = item['secure_progressive_url']
        else:
            continue
        parsed_list.append(parsed)
    parsed_list.reverse()
    database = {'store': parsed_list}

    for i in parsed_list:
        sys.stdout.write("%s %s %s\n" % (i['id'], i['url'], i['thumbnail']))
        sys.stdout.flush()

    dfile = file("database.json", 'w')
    dfile.write(json.dumps(database))
    dfile.close()

if __name__ == "__main__":
    main()
