import pandas as pd

def main():
    # Reads every table in the webpage into a list of DataFrames
    result = pd.read_html("https://en.wikipedia.org/wiki/OpenAI")
    print("First table:")
    print(result[0])
    print("Second table:")
    print(result[1])

if __name__ == "__main__":
    main()