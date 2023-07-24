# Horsemapp QR Code Generator

This python script takes an excel sheet with id, name, and phone number and generates
a QR code for each tuple. See the example below:

![](images/sample.png)

Scanning the QR code opens a contact card with their first name and number. 

## Installation

Mac: 

1. Please download the entire folder from Github.
![](images/instruction1.png)


2. Then open a new Terminal at the folder.
![](images/instruction2.png)


3. In the terminal copy the following text and press enter.
```bash
pip install -r requirements.txt

# or 

pip3 install -r requirements.txt
```

## Usage

1. First download the User Export from Looker Studio.
![](images/instruction3.png)


2. Rename this file as export.csv and store it in the QRCodeGenerator folder.
![](images/instruction4.png)

To run the script enter the following code in the previously opened terminal and the QR codes 
will be generated.

```bash
python myscript.py

# or 

python3 myscript.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)