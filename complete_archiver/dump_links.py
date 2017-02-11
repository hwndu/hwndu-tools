import json

def main():
    data = json.load(file("database.json"))
    parsed = data['store']
    for i in parsed:
        print "https://storage.googleapis.com/hwndu-video-backups/cvideo/%s" % i['id']

if __name__ == "__main__":
    main()
