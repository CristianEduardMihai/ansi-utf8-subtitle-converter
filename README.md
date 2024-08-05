# ANSI-UTF8 Subtitle Converter

A lot of subtitles are available in the ANSI encoding, which can cause issues with displaying diacritics correctly. This tool converts ANSI-encoded subtitles to UTF-8, ensuring that characters like `ț` are displayed correctly instead of incorrect representations like `þ`.

## Features

- **Automatic Character Mapping**: Automatically maps incorrect ANSI characters to their correct UTF-8 counterparts.

- **Custom Language Support**: Easily create character maps for different languages.

- **Batch Processing**: Convert multiple subtitle files at once.

## Installation

*To use this tool, you'll need to have Python and PIP installed on your system.

1. Clone or download the repository to your local machine.

2. Install the required dependencies using the following command:

```bash
pip3 install -r requirements.txt
```

## Usage

### Creating a Character Map for Your Language

This tool comes with a pre-configured character map for Romanian. If you need to create a character map for another language:

1. Examine around 50 lines of any subtitle file in your language, noting any incorrect characters.

2. Map each incorrect character to its correct UTF-8 equivalent.

Note: You don't need to worry about uppercase characters. The code automatically handles capitalization.

### Converting Subtitles

To convert your subtitle files:

1. Place any `.srt` file you want to convert into the `input` directory.

2. Run the conversion script. The script processes the files and saves the converted versions in the `output` directory, appending `_converted` to the filename.

### Example

If you have a subtitle file named `example.srt` in the `input` directory, run the conversion script. You will find the converted file named `example_converted.srt` in the `output` directory.