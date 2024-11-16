import os
import json
import re

# Usage example
input_dir = 'input'
character_map_file = 'charmaps/romanian.json'
output_dir = 'output'

# Remove .gitkeep files from input and out directories
for file in os.listdir(input_dir):
    if file == '.gitkeep':
        os.remove(os.path.join(input_dir, file))

for file in os.listdir(output_dir):
    if file == '.gitkeep':
        os.remove(os.path.join(output_dir, file))

def read_srt_file(srt_file):
    with open(srt_file, 'r', encoding='ansi') as file:
        return file.read()

def convert_srt_to_utf8(srt_file, character_map_file):
    srt_content = read_srt_file(srt_file)

    # Read the character map JSON file
    with open(character_map_file, 'r', encoding='utf-8') as file:
        character_map = json.load(file)

    # Split content into lines
    lines = srt_content.splitlines()

    # Replace ansi values with utf characters
    for i, line in enumerate(lines):
        for char_map in character_map['characters']:
            ansi_char = char_map['ansi']
            utf_char = char_map['utf']
            
            # Check if the line starts with a tag
            match = re.match(r'(<[^>]+>)(.*)', line)
            if match:
                tag, rest_of_line = match.groups()
                rest_of_line = rest_of_line.replace(ansi_char, utf_char)
                rest_of_line = rest_of_line.replace(ansi_char.upper(), utf_char.upper())
                line = tag + rest_of_line
            else:
                line = line.replace(ansi_char, utf_char)
                line = line.replace(ansi_char.upper(), utf_char.upper())
        
        lines[i] = line

    # Join lines back into a single string
    utf8_content = '\n'.join(lines)

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Write the converted content to a new .srt file in the output directory
    converted_file = os.path.join(output_dir, os.path.basename(srt_file))
    with open(converted_file, 'w', encoding='utf-8') as file:
        file.write(utf8_content)

    print(f"Conversion complete. Converted file saved as {converted_file}")

for file in os.listdir(input_dir):
    if file.endswith('.srt'):
        srt_file = os.path.join(input_dir, file)
        convert_srt_to_utf8(srt_file, character_map_file)