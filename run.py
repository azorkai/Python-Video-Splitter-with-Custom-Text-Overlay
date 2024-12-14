from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.config import change_settings
import os
from datetime import datetime

# Specify the path to ImageMagick
change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})

# Input and output settings
input_video = "input.mp4"  # Input video file
output_base_dir = "output_parts"  # Directory to save all video parts
text_top = "Up Text"  # Text to display at the top
text_bottom = "Bottom Text!"  # Text to display at the bottom
part_duration = 60  # Duration for each video segment (in seconds)
output_resolution = (720, 1280)  # Vertical resolution suitable for TikTok

def create_unique_output_dir(base_dir):
    """
    Create a unique directory for saving output files each time the script is run.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    unique_dir = os.path.join(base_dir, timestamp)
    os.makedirs(unique_dir, exist_ok=True)
    return unique_dir

def process_and_split_video(input_video, output_base_dir, text_top, text_bottom, part_duration, output_resolution):
    # Create a unique directory for the output files
    output_dir = create_unique_output_dir(output_base_dir)
    print(f"Videos will be saved in the directory: {output_dir}")

    video = VideoFileClip(input_video)
    total_duration = video.duration
    num_parts = int(total_duration // part_duration) + (1 if total_duration % part_duration > 0 else 0)

    print(f"Total video duration: {total_duration:.2f} seconds.")
    print(f"Number of segments to create: {num_parts}.")

    for i in range(num_parts):
        start_time = i * part_duration
        end_time = min((i + 1) * part_duration, total_duration)
        video_part = video.subclip(start_time, end_time)

        # Resize the video without altering its aspect ratio
        video_resized = video_part.resize(height=output_resolution[1] * 0.5)
        video_positioned = CompositeVideoClip(
            [video_resized.set_position("center")], size=output_resolution
        )

        # Add top text
        top_text = TextClip(
            text_top, fontsize=50, color="white", bg_color="black", size=(output_resolution[0], 60)
        ).set_position(("center", 180)).set_duration(video_part.duration)

        # Add bottom text
        bottom_text = TextClip(
            text_bottom, fontsize=50, color="white", bg_color="black", size=(output_resolution[0], 60)
        ).set_position(("center", output_resolution[1] - 240)).set_duration(video_part.duration)

        # Combine the video with the text layers
        final_video = CompositeVideoClip([video_positioned, top_text, bottom_text], size=output_resolution)

        # Define the output file name
        output_file = os.path.join(output_dir, f"part_{i + 1}.mp4")

        # Save the video
        print(f"Processing segment {i + 1}/{num_parts}...")
        final_video.write_videofile(
            output_file,
            codec="libx264",
            audio_codec="aac",
            bitrate="3000k",  # High-quality output
            preset="medium"
        )
        print(f"Segment {i + 1} successfully saved: {output_file}")

    print("All segments have been successfully processed and saved.")

# Call the processing function
process_and_split_video(input_video, output_base_dir, text_top, text_bottom, part_duration, output_resolution)
