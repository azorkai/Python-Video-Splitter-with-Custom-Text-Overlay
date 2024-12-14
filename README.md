
# Video Splitter for TikTok and Short Form Content

## Description
This Python script allows you to split a video into multiple parts, add custom text at the top and bottom of each segment, and resize it to fit a vertical resolution suitable for platforms like TikTok. Each video segment is saved as a separate file in a unique directory for each run, ensuring organized outputs.

With the help of the `moviepy` library and ImageMagick for text rendering, this script makes it easy to process long videos into bite-sized content with stylish captions.

---

## Features
- **Split Videos:** Automatically divides the input video into smaller segments of a specified duration.
- **Customizable Text:** Add top and bottom text overlays to each video segment.
- **Vertical Resolution:** Resize videos to a vertical resolution (720x1280 by default) suitable for TikTok.
- **Organized Output:** Saves video segments into uniquely named directories for easy file management.

---

## Requirements
- Python 3.7 or later
- Required Python libraries: `moviepy`
- ImageMagick installed on your system

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/azorkai/Python-Video-Splitter-with-Custom-Text-Overlay.git
   cd video-splitter-tiktok
   ```

2. **Install Dependencies:**
   ```bash
   pip install moviepy
   ```

3. **Install ImageMagick:**
   - Download and install [ImageMagick](https://imagemagick.org/script/download.php) for your operating system.
   - Note the installation path for later configuration.

---

## Configuration

1. Update the path to ImageMagick in the script:
   ```python
   change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})
   ```
   Adjust the path based on your ImageMagick installation.

2. Set the following parameters as needed:
   - `input_video`: Path to the input video file.
   - `output_base_dir`: Base directory to save the video segments.
   - `text_top`: Custom text for the top overlay.
   - `text_bottom`: Custom text for the bottom overlay.
   - `part_duration`: Duration (in seconds) for each video segment.
   - `output_resolution`: Output resolution, default is `(720, 1280)`.

---

## Usage

Run the script using:
```bash
python run.py
```
The script will process the input video, split it into parts, add overlays, and save the output files in a unique directory under the specified base directory.

---

## Example

Suppose you have a video named `input.mp4` and you want to split it into 60-second parts with the following settings:
- Top text: "Up Text"
- Bottom text: "Bottom Text!"
- Vertical resolution: `(720, 1280)`

Modify the script parameters and run it. The output directory will look like this:
```
output_parts/2024-12-14_12-00-00/
  - part_1.mp4
  - part_2.mp4
  - ...
```

---

## Contributing
Feel free to fork the repository, submit pull requests, or suggest improvements via issues.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
- The amazing [MoviePy](https://zulko.github.io/moviepy/) library for video editing.
- [ImageMagick](https://imagemagick.org/) for high-quality text rendering.
