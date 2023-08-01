import os
import subprocess

def batch_convert_trec_to_mp4(input_folder, output_folder):
    # Check if input and output folders exist
    if not os.path.exists(input_folder):
        print("Input folder does not exist.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all .trec files in the input folder
    trec_files = [file for file in os.listdir(input_folder) if file.endswith(".trec")]

    # Loop through each .trec file and convert it to .mp4
    for trec_file in trec_files:
        input_path = os.path.join(input_folder, trec_file)
        output_path = os.path.join(output_folder, os.path.splitext(trec_file)[0] + ".mp4")

        # Use subprocess to call ffmpeg command-line tool
        try:
            subprocess.run(["ffmpeg", "-i", input_path, output_path])
            print(f"Successfully converted {trec_file} to {os.path.basename(output_path)}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {trec_file}: {e}")

if __name__ == "__main__":
    input_folder = "C:\\path\\to\\trec_files"  # Replace with the path to the folder containing .trec files
    output_folder = "C:\\path\\to\\output_folder"  # Replace with the path to the folder where .mp4 files will be saved

    batch_convert_trec_to_mp4(input_folder, output_folder)