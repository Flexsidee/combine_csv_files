### How to use

1. Pull the repository to your local machine.
2. Install Python 3.8 or higher.
3. Install the required packages by running `pip install csv` in the command line.
4. Place all the CSV files you want to combine in the `inputs` directory.
5. Run the `combine.py` script.
6. The combined CSV file will be saved in the `outputs` directory.
7. The combined CSV file will be named `combined_csvs.csv` by default. You can change this by editing line 7 of the `combine.py` script.
8. The combined CSV file will contain a header row and a data row for each CSV file. If you want to remove the header row from each CSV file, set `skip_header` to `True` on line 8 of the `combine.py` script.
9. If you want to combine CSV files from a different directory, change the value of `directory` on line 4 of the `combine.py` script.
10. If you want to combine CSV files with a different file extension, change the value of `".csv"` on line 5 of the `combine.py` script.
11. If you want to combine CSV files with a different delimiter, change the value of `","` on line 6 of the `combine.py` script.
12. If you want to combine CSV files with a different encoding, change the value of `"utf-8"` on line 7 of the `combine.py` script.
