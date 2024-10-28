import tools

if __name__ == "__main__":
    required = input("Enter:\n'playlist' to download playlist\n'video' to download a video\n'channel' to download all videos from a channel\n'voice' for only voice file\n'picture' for picture only\nYour's choice: ")
    if required=="playlist":
        url = input("Enter the url for whole playlist\nurl:")
        tools.playlist(url=url)
    elif required=="video":
        url = input("Enter the url of the video\nurl:")
        tools.video(url=url)
    elif required=="channel":
        url = input("Enter the url of the channel\nurl:")
        tools.channel(url=url)
    elif required == "voice":
        url = input("Enter the url of the video\nurl:")
        tools.video_voice_only(url)
    elif required == "picture":
        url = input("Enter the url of the video\nurl:")
        tools.picture_only(url)    
    else:
        print("Invalid")