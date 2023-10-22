import utils
import click
from PIL import Image


@click.command("tvfx")  # timestamped video frame 'xtractor
@click.argument("video-path", type=click.Path(exists=True, file_okay=True, dir_okay=False))
@click.argument("start-timestamp", type=click.FLOAT)
@click.argument("timestamp", type=click.FLOAT)
@click.option(
    "--save",
    help="Save extracted image to provided path.",
    type=click.Path(dir_okay=False),
    default=None,
)
@click.option(
    "--show", help="Whether to show the extracted image.", type=click.BOOL, default=False, show_default=True
)
def run(video_path: str, start_timestamp: float, timestamp: float, save: str | None, show: bool) -> None:
    """tvfx: (T)imestamped (V)ideo (F)rame e(X)tractor by mapping overlaid timestamps
    to actual video time.

    VIDEO_PATH:         Absolute path or a URL to a timestamped video.
    START_TIMESTAMP:    Overlaid timestamp at initial frame of the video.
    TIMESTAMP:          Timestamp at which the corresponding image is extracted.
    """
    extracted_img = Image.open(
        utils.extract_frame(video_path, at_secs_since_start=timestamp - start_timestamp)
    )
    if save is not None:
        with open(save, "wb") as fs:
            extracted_img.save(fs)
    if show:
        extracted_img.show()
    extracted_img.close()


if __name__ == "__main__":
    run()
