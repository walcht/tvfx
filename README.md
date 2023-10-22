# About

![cctv image with a timestamp overlay in seconds in bottom right](https://user-images.githubusercontent.com/89390465/277192842-820760f6-3ef8-423f-8566-8b0a91cb28ee.png)

The image above showcases an example of a timestamped image. A timestamped video
is a video where each frame has a timestamp overlay. The objective of this tool
is to make it extremely simple and fast to extract frames by their overlay timestamps.

## Assumptions

1. It is assumed that *for any frame in the timestamped video, the overlay timestamp
has a __constant__ and __positive__ offset to the actual video time of the frame.*

## Installation

1. First make sure that ```ffmpeg``` is installed on your machine. Refer to [official installation guide](https://ffmpeg.org/download.html)
2. Make sure to have **Python >= 3.9.0**
3. Run:

    ```Shell
    pip3 install -r requirements.txt
    ```

4. Ready to go 😃

## Usage

You can either use the GUI (yet to be implemented) or the provided CLI. For help
on CLI usage, type:

```Shell
python3 tvfx.py --help
```

Which prints the following output:

```Shell
Usage: tvfx.py [OPTIONS] VIDEO_PATH START_TIMESTAMP TIMESTAMP

  tvfx: (T)imestamped (V)ideo (F)rame e(X)tractor by mapping overlaid timestamps
  to actual video time.

  VIDEO_PATH:         Absolute path or a URL to a timestamped video.
  START_TIMESTAMP:    Overlaid timestamp at initial frame of the video.
  TIMESTAMP:          Timestamp at which the corresponding image is extracted.

Options:
  --save FILE     Save extracted image to provided path.
  --show BOOLEAN  Whether to show the extracted image.  [default: False]
  --help          Show this message and exit.
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
See LICENSE.txt file for more info.
