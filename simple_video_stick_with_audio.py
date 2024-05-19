import os
from datetime import datetime
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip
from moviepy.video.fx.all import speedx

def get_video_files(directory):
    """
    Returns a list of video file paths from the specified directory.
    """
    supported_formats = ('.mp4', '.avi', '.mov', '.mkv', '.flv')
    return [os.path.join(directory, file) for file in os.listdir(directory) if file.lower().endswith(supported_formats)]

def scale_video(video, target_size):
    """
    Scales the video to match the target size while maintaining the aspect ratio.
    """
    return video.resize(newsize=target_size)

def apply_slow_motion(video, factor):
    """
    Applies slow motion to the video by the given factor.
    """
    return speedx(video, factor=factor)

def concatenate_videos(video_paths, output_path, audio_path=None, slow_motion_factor=None):
    """
    Concatenates videos from the list of video paths and saves the output video.
    Optionally adds an audio track and applies slow motion.
    """
    if not video_paths:
        raise ValueError("No video paths provided")

    # Load the first video and use its size as the baseline
    first_clip = VideoFileClip(video_paths[0])
    target_size = first_clip.size

    # Apply slow motion if the factor is provided
    if slow_motion_factor:
        first_clip = apply_slow_motion(first_clip, slow_motion_factor)

    # Load and scale subsequent videos
    clips = [first_clip] + [scale_video(apply_slow_motion(VideoFileClip(path), slow_motion_factor) if slow_motion_factor else VideoFileClip(path), target_size) for path in video_paths[1:]]

    # Concatenate the video clips
    final_clip = concatenate_videoclips(clips)

    # Add audio if provided
    if audio_path:
        audio_clip = AudioFileClip(audio_path)
        final_clip = final_clip.set_audio(audio_clip)

    # Write the output video to the specified path
    final_clip.write_videofile(output_path, codec="libx264")

def generate_output_path(base_dir, prefix="final_video"):
    """
    Generates a unique output file path using the current date and time.
    """
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prefix}_{current_time}.mp4"
    return os.path.join(base_dir, filename)

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
