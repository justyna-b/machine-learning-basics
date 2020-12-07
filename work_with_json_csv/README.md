# WORK WITH DATA IN JSON OR CSV FORMAT

## Write JSON

Write data into given file (encode):

```bash
json.dump(data, write_file)
```

Save data as String value:

``bash
json.dumps(data)
```
This function can receive argument indent=number. Thanks to that, you can set the indentation by given number of space chars.

## Deserializing JSON

load() and loads() functions turning JSON encoded data into Python objects (decode)

```bash
json.loads(simple_json)
```

## Fetch data from API

```bash
requests.get(url)
```

Send request to API and receive response (save to variable)
response.text parameter take text value of response (without code status for example)


## WRITE AND READ CSV

Read csv file using csv (first open() txt)

```bash
csv.reader(csv_file, delimiter=',')
```

Write data to csv using csv

```bash
csv_file_to_add.writerow(['data'])
```

Read data from csv file using pandas

```bash
pandas.read_csv()
```

Write data to csv file

```bash
df.to_csv('file.csv')
```