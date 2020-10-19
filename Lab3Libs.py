import sys
import json
import yaml
import time



def main():

    outputFile = open("LibWeekday.yaml", "w", encoding="utf-8")

    with open('Weekday.json', encoding='utf-8') as fh:
              data = json.load(fh)
    outputFile.write(yaml.dump(data, allow_unicode=True))

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("---With Libs %s seconds ---" % (time.time() - start_time))