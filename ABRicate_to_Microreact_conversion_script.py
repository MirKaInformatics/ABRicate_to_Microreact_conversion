import pandas as pd

input_file = input("Enter the input file name (with csv extension): ")

df = pd.read_csv(input_file)

rows, cols = df.shape

for row in range(0, rows):
    for col in range(2, cols):
        # If the current cell contains a ".", replace it with "0"
        if df.iat[row, col] == ".":
            df.iat[row, col] = 0
        # If the current cell does not contain "0", replace it with "1"
        elif df.iat[row, col] != 0:
            df.iat[row, col] = 1

df_copy = df.iloc[:, 2:]

df_copy.columns = [col + "__color" for col in df_copy.columns]

df = pd.concat([df, df_copy], axis=1)

present_color = input("Enter the HEX code for present genes: ")

absent_color = input("Enter the HEX code for absent genes: ")

for col in df.columns:
    if col.endswith("__color"):
        df[col] = df[col].apply(lambda x: present_color if x == 1 else absent_color)

output_file = input("Enter the output file name (with csv extension): ")

df.to_csv(output_file, index=False)

print("File converted successfully.")
