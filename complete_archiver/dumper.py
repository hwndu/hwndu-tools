import json

def main():
    data = json.load(file("database.json"))
    parsed = data['store']
    for i in parsed:
        print "%s %s %.2fHRS" % (i['streamed_at'], i['id'], i['original_duration']/1000.0/60/60)

if __name__ == "__main__":
    main()
