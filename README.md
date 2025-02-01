# Game Compilation Script

This Python script automates the process of finding, copying, and compiling game directories containing Go source files. It also generates metadata in JSON format.

## Features
- Finds all directories containing `game` in their name.
- Copies these directories to a target location.
- Compiles `.go` source files inside the copied directories.
- Generates a `metadata.json` file listing all game directories and their count.

## Prerequisites
- Python 3.x
- Go installed and accessible via the command line

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```
2. Ensure you have Python and Go installed.

## Usage
Run the script with:
```bash
python script.py <source_directory> <target_directory>
```
- `<source_directory>`: The directory where game folders are located.
- `<target_directory>`: The directory where the processed game folders will be stored.

### Example:
```bash
python script.py games/ compiled_games/
```

## Script Breakdown
- **find_all_game_paths(source)**: Locates all directories containing `game` in their name.
- **create_dir(path)**: Creates a directory if it doesn’t exist.
- **copy_and_overwrite(sources, dest)**: Copies game directories to the target location.
- **make_json_metadata_file(path, game_dirs)**: Generates a JSON file listing all found games.
- **get_name_from_path(paths, to_strip)**: Cleans up directory names.
- **compile_game_code(path)**: Searches for `.go` files and compiles them.
- **run_command(command, path)**: Executes shell commands in the given directory.
- **main(source, target)**: Orchestrates the script flow.

## Output
- Copied and compiled game directories inside `<target_directory>`.
- A `metadata.json` file inside `<target_directory>` with details of the processed games.

## License
This project is licensed under the MIT License.

## Contributing
Feel free to open issues or submit pull requests for improvements.
