import subprocess
from typing import NamedTuple
from io import BytesIO


class VideoInfo(NamedTuple):
    avg_frame_rate: float  # in frames-per-second
    r_frame_rate: float  # maximum frame rate
    duration: float  # in seconds
    nb_frames: int
    width: int
    height: int


def extract_info(input_video_path: str) -> VideoInfo:
    command = (  # do NOT remove trailing spaces!
        "ffprobe -hide_banner -loglevel level+error -select_streams v:0 -show_entries "
        + "stream=avg_frame_rate,r_frame_rate,duration,nb_frames,width,height "
        + f"-of default=noprint_wrappers=1 -i {input_video_path}"
    )
    proc = subprocess.run(command.split(" "), capture_output=True, check=True, text=True)
    avg_frame_rate, r_frame_rate, duration, nb_frames, width, height = (None, None, None, None, None, None)
    for line in proc.stdout.splitlines():
        _split = line.split("=")
        if _split[0] == "avg_frame_rate":
            division_split = _split[1].split("/")
            avg_frame_rate = int(division_split[0]) / int(division_split[1])
        elif _split[0] == "r_frame_rate":
            division_split = _split[1].split("/")
            r_frame_rate = int(division_split[0]) / int(division_split[1])
        elif _split[0] == "duration":
            duration = float(_split[1])
        elif _split[0] == "nb_frames":
            nb_frames = int(_split[1])
        elif _split[0] == "width":
            width = int(_split[1])
        elif _split[0] == "height":
            height = int(_split[1])
        else:
            raise RuntimeError(f"Unexpected output encountered: {_split[0]}")
    if (
        avg_frame_rate is None
        or r_frame_rate is None
        or duration is None
        or nb_frames is None
        or width is None
        or height is None
    ):
        raise RuntimeError("Some expected outputs were not found")
    return VideoInfo(avg_frame_rate, r_frame_rate, duration, nb_frames, width, height)


def extract_frame(input_video_path: str, at_secs_since_start: float) -> BytesIO:
    command = (  # do NOT remove trailing spaces!
        f"ffmpeg -hide_banner -loglevel quiet -ss {at_secs_since_start} -i {input_video_path} "
        + "-frames:v 1 -q:v 2 -f singlejpeg pipe:1"
    )
    proc = subprocess.run(
        args=command.split(" "),
        capture_output=True,
        check=True,
    )
    return BytesIO(proc.stdout)
