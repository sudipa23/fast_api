import glob

  
video_list = glob.glob('*.3gp')
cleaned_mp4s = [files.replace("\\", "/") for files in video_list]

print(cleaned_mp4s[0])


