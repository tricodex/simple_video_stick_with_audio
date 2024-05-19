## README.md

# Simple Video Stick with Audio

This Python script concatenates multiple video files, scales them to a uniform size, optionally applies a slow-motion effect, and adds an audio track. The script uses MoviePy for video manipulation and requires FFmpeg for video processing.

## Features

- Concatenates multiple video files from a directory or a predefined list.
- Scales all videos to match the resolution of the first video.
- Optionally applies a slow-motion effect to the videos.
- Optionally adds an audio track to the final video.
- Generates a uniquely named output file using the current date and time.

## Requirements

- Python 3.6 or higher
- MoviePy
- FFmpeg

## Installation

1. Install MoviePy using pip:

   ```sh
   pip install moviepy
   ```

2. Install FFmpeg and ensure it is added to your system's PATH. Follow the installation instructions from the [FFmpeg website](https://ffmpeg.org/download.html).

## Usage

1. Clone or download the repository.

2. Modify the `main()` function in the script to set the correct input directory, output directory, audio path, and slow motion factor.

3. Run the script:

   ```sh
   python simple_video_stick_with_audio.py
   ```

### Example Configuration

```python
def main(directory=True):
    if directory:
        # Define the input directory or list of video paths
        input_directory = "input_dir"
        video_paths = get_video_files(input_directory)
    else:
        # Alternative: use a predefined list of video paths
        video_paths = ["path/to/video1.mp4", "path/to/video2.mp4", ...]

    # Define the output base directory and optional audio path
    output_base_dir = "output"
    audio_path = "path/to/audio"  # Set to None if no audio is to be added

    # Ensure the output directory exists
    os.makedirs(output_base_dir, exist_ok=True)

    # Generate a unique output file path
    output_path = generate_output_path(output_base_dir)

    # Define the slow motion factor (e.g., 0.5 for half speed)
    slow_motion_factor = 0.7  # Set to None for no slow motion

    # Concatenate videos and optionally add audio
    concatenate_videos(video_paths, output_path, audio_path, slow_motion_factor)

if __name__ == "__main__":
    main(directory=False)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Notes

- Ensure FFmpeg is installed and accessible via the system's PATH.
- Adjust the `input_directory`, `output_base_dir`, `audio_path`, and `slow_motion_factor` variables as necessary.
- The script generates a uniquely named output file based on the current date and time to avoid file name conflicts.