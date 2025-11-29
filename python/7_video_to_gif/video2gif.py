from moviepy.editor import VideoFileClip

def video2gif():
    """
    Converts a video file to a GIF.
    """
    # Load the video file
    videoClip = VideoFileClip("input_video.mp4")
    videoClip.write_gif("output_video.gif")
    videoClip.close()

video2gif()