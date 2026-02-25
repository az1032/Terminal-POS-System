# RetroPOS: Python OpenCV Barcode Scanner and POS System

This project is a terminal application that uses Python and OpenCV to turn a computer's webcam into a barcode scanner, operating on a basic point-of-sale (POS) logic in the background. 

Instead of relying on heavy and complex databases, the system is designed to be as lightweight and fast as possible by reading and writing data directly to a `.txt` file.

## Features

* Real-Time Barcode Scanning: Instant barcode detection and decoding via the camera using the pyzbar library.
* Cashier / POS Mode: Checks if the scanned barcode exists in the system. If registered, it prints the product name and price, and adds it to the cart total.
* Product Registration Mode: When an unregistered product is scanned, it prompts the user for the product name and pricing details, then saves it to the database (txt file).
* Dynamic Terminal Interface: Upon launching, the console clears automatically and resizes itself (65x25) to resemble a standard cash register panel.
* Memory Optimization: File I/O operations are optimized using cursor positioning (seek) logic to prevent memory leaks and overloading the computer during infinite camera loops.

## Installation and Requirements

To run this project, Python 3.x must be installed on your system. You also need to install the required image processing and barcode decoding libraries.

Run the following command in your terminal to install the dependencies:
pip install opencv-python pyzbar

## Database Structure (barkodlar.txt)

The system stores its data in a file named `barkodlar.txt`. If you are running the program for the first time, simply create an empty text file with this name in the project directory.

Each registered product is stored in the text file using the following format:
ProductName-CostPrice-SellingPrice-BarcodeNumber
(Example: Chocolate Bar-10-15-8691234567890)

## Usage

Built-in terminals in some IDEs might override the screen resizing (mode con) commands. To experience the interface as intended, it is highly recommended to run the script directly from the Windows Command Prompt (CMD).

1. Navigate to your project folder.
2. Type cmd in the folder's address bar and press Enter to open the command prompt.
3. Start the system by typing `python main.py`.

### Controls:
* In Sales Mode: Press the ENTER key to finish the transaction and print the total receipt.
* In Registration Mode: Press the ESC key to close the camera.

## Developer Notes

This project was developed to practice and understand fundamental file management (I/O), image processing with OpenCV, nested loop algorithms, and state flags. It provides a solid foundation and is completely open to further development and new features.
