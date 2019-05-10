"""
1. Get a JSON representation of your own github account. 
2. Serialize the json object and save to a file.
3. Deserialize the data and save it to a CSV file.
4. try to open the file in excell og google spreadsheet
"""
import urllib.request, json

with urllib.request.urlopen("https://github.com/marcuselmgreen") as url:
    data = json.loads(url.read().decode())
    print(data)
