import pafy

a=int(input('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@                              Choose Any topic:                                           @\n@                  Press 1 :Download a Youtube vedio:                          @\n@            Press 3 ; Download a Audio File for youtube vedio:        @\n@      Press 2 : Read a Information realated to the youtube vedio: @\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\nEnter choose number:'))
if a==2:
    # url of video
    print("                  @READING INFORMATION TOOL@                           ")
    
    url =input("Enter Any Youtube Video URL:")
    video = pafy.new(url) 
    print("VIDEOTITLE=>", video.title) 
    print("VIDEORATING=>", video.rating) 
    print("VIDEOVEIWCOUNTING=>", video.viewcount) 
    print("VIDEOAUTHOR=>", video.author,"VIDEOLENGTH=>", video.length) 
    print("VIDEODURATION=>", video.duration,"VIDEOLIKES=>", video.likes,"VIDEODISLIKES=>", video.dislikes,"VIDEODESCRIPTION=>", video.description)

if a == 1:
    print("                  @YOUTUBE VIDEO DOWNLOADER TOOL@                           ")
    url =input("Enter Any Youtube Video URL:")
    video = pafy.new(url) 
    print("VIDEOTITLE=>", video.title)
    streams = video.streams 
    for i in streams:
        print(i) 
    best = video.getbest() 
    print(best.resolution, best.extension) 
    best.download()
if a == 3:
    print("                  @YOUTUBE AUDIO DOWNLOADER TOOL@                           ")
    url =input("Enter Any Youtube Video URL:")
    video = pafy.new(url)
    print("VIDEOTITLE=>", video.title)
    bestaudio = video.getbestaudio() 
    bestaudio.download() 


