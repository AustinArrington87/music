from moviepy.editor import VideoFileClip

def convert_mov_to_mp4(mov_file_path, mp4_file_path):
    # Load the .mov video file
    clip = VideoFileClip(mov_file_path)
    
    # Write the clip as an .mp4 file
    clip.write_videofile(mp4_file_path, codec='libx264', audio_codec='aac')

# Example usage
mov_file_path = '/Users/austinarrington/Desktop/data-scripts-main/music/tae1.mov'
mp4_file_path = '/Users/austinarrington/Desktop/data-scripts-main/music/tae1.mp4'

convert_mov_to_mp4(mov_file_path, mp4_file_path)
