# generate-tool

Generate script based on user's requirements.

## Usage

`python3 generate_tool.py`

```
usage: generate_tool.py [-h] -k API_KEY [-v {3.5-turbo,4,4-turbo-preview}] -content KEY_CONTENT -t SCRIPT_TYPE -f
                        SCRIPT_FILE

Generate script based on user's requirements.

options:
  -h, --help            show this help message and exit
  -k API_KEY, --api_key API_KEY
                        API key for OpenAI.
  -v {3.5-turbo,4,4-turbo-preview}, --api_version {3.5-turbo,4,4-turbo-preview}
                        API version to use: GPT-3.5 Turbo, GPT-4, or GPT-4 Turbo Preview. Default is GPT-4 Turbo Preview.
  -content KEY_CONTENT, --key_content KEY_CONTENT
                        The content to be included in the prompt.
  -t SCRIPT_TYPE, --script_type SCRIPT_TYPE
                        The type of script to generate.
  -f SCRIPT_FILE, --script_file SCRIPT_FILE
                        The script file name to generate.
```

## Example

[export database structure](https://github.com/liCells/generate-tool/blob/main/examples/export_database_structure.py)
