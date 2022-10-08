mp4files = yt.filter('mp4')

# get the video with the extension and
# resolution passed in the get() function
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)