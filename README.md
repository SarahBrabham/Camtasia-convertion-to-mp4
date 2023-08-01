# Batch Convert .trec to .mp4 using Python and FFmpeg
This script will batch convert .trec files from Camtasia to .mp4 files.



## Prerequisites
Before running the script, ensure that you have the following installed:

1. **Python 3**: The script is written in Python, so you need to have [Python 3](https://www.python.org/downloads/) installed on your system.

2. **FFmpeg**: [FFmpeg](https://www.ffmpeg.org/) is a multimedia framework that can handle audio, video, and other multimedia files. Make sure you have FFmpeg installed and added to your system's PATH variable so that the script can use it. 

## How to Use
1. Clone or download the repository to your local machine.

2. Install the required dependencies:

    *No additional dependencies required, as the script uses built-in Python modules.*

3. Organize your .trec files:  
Place all the .trec files you want to convert into a single folder. Note down the path to this input folder.

4. Choose the output folder:  
Decide on the folder where you want to save the converted .mp4 files. Note down the path to this output folder.

5. Modify the Python script:  
Open the `trec_to_mp4.py` file in a text editor. Look for the following lines:

    ```python
    if __name__ == "__main__":
        input_folder = "/path/to/trec_files"  # Replace with the path to the folder containing .trec files
        output_folder = "/path/to/output_folder"  # Replace with the path to the folder where .mp4 files will be saved

        batch_convert_trec_to_mp4(input_folder, output_folder)
    ```

    Replace `/path/to/trec_files` with the path to the folder containing your .trec files and `/path/to/output_folder` with the path to the folder where you want to save the converted .mp4 files.

6. Run the script:

    - For Mac:

        - Open Terminal (you can find it in Applications > Utilities > Terminal).

        - Navigate to the directory containing the `trec_to_mp4.py` file using the `cd` command.

        - Run the script using the following command:

            ```
            python3 trec_to_mp4.py

            ```

    - For PC:

        - Open Command Prompt (you can find it by searching for "Command Prompt" in the Start menu).

        - Navigate to the directory containing the `trec_to_mp4.py` file using the `cd` command.

        - Run the script using the following command:


            ```
            python trec_to_mp4.py
            ```

    The script will start converting .trec files to .mp4 in the specified output folder. The converted files will have the same filenames as the original .trec files but with the .mp4 extension.

7. Monitor the progress:  
The script will display messages indicating the progress of the conversion for each file. It will notify you if any errors occur during the process.

## Note
- Change input and output paths to include "C:\\" on Windows, must have double "\\" in-between as directory separators. For Mac, use a single "/" in-between all directory separators.

- Ensure that you have enough disk space in the output folder to accommodate the converted .mp4 files.

- Always double-check the input and output folder paths to avoid any accidental data loss.

- This script assumes that the .trec and .mp4 files are compatible with FFmpeg. If you encounter any issues with specific file formats or codecs, you may need to adjust the script or update FFmpeg accordingly.

- It's essential to have a basic understanding of FFmpeg and Python to modify and troubleshoot the script as needed.

### Credits
Made by Sarah Brabham, with use of ChatGPT.