# Script takes csv file with ASCII to Unicode mappings and generates an .XCompose file with corresponding bindings

import csv
import sys

ignore_backslash = True

def generate_xcompose(csv_file, csv_alias_file):
    # Load aliases into a dictionary
    aliases = {}
    with open(csv_alias_file, newline='') as aliasfile:
        alias_reader = csv.DictReader(aliasfile)
        for row in alias_reader:
            aliases[row['ASCII']] = row['Alias']

    # Debugging aliases
    # print("Aliases loaded:")
    # for ascii_char, alias in aliases.items():
    #     print(f"{ascii_char} -> {alias}", file=sys.stderr)

    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print("include \"%L\"\n")
        print("\n### TLA+ Unicode Symbols ###")
        for row in reader:
            ascii_sequences = row['ASCII'].split(';')
            unicode_char = row['Unicode']
            for ascii_sequence in ascii_sequences:
                if ignore_backslash and any(char.isalpha() for char in ascii_sequence):
                    ascii_sequence = ascii_sequence.replace('\\', '')
                # Replace each character with its alias if it exists
                wrapped_sequence = ' '.join(f"<{aliases.get(char, char)}>" for char in ascii_sequence)
                print(f"<Multi_key> {wrapped_sequence} : \"{unicode_char}\"")
        print("#############################\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python translate.py <input_csv_file>", file=sys.stderr)
        sys.exit(1)

    input_csv_file = sys.argv[1]
    generate_xcompose(input_csv_file, 'key-alias.csv')