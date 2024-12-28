<div align="center">
<a href="https://github.com/Yeadee/Toffee">
<img src="https://toffeelive.com/logo.svg" alt="Logo" width="400px">
</a>
<br/>

</div>

## About The Project

A simple script to automatically update Toffee channels list with cookies every 4 hours.

## Key Features

- Fully open-source (except the key and api url for security purposes).
- Premium events are also available.
- provides ready-to-use m3u file for NS player.
- provides data as json for developers' use.

## How To Use

- Use [this](https://raw.githubusercontent.com/Yeadee/Toffee/main/toffee_channel_data.json) link for TV data.

- script to obtain m3u8 information:
  ```python
  import requests
  link="https://raw.githubusercontent.com/Yeadee/Toffee/main/toffee_channel_data.json"
  response=requests.get(link).json()
  name=response["name"]
  for channel in response["channels"]:
    url=channel["link"]
    headers={"cookie":channel["cookie"]}
    break
  main_response=requests.get(url,headers=headers).text
  print(main_response)
  ```
>Prerequisite: You need to have [Python](https://www.python.org) installed on your machine.
- Output:
```
#EXTM3U
#EXT-X-VERSION:3

#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1024000,RESOLUTION=1280x720
../slang/cnn_576/cnn_576.m3u8?bitrate=1000000&channel=cnn_576&gp_id=
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=768000,RESOLUTION=854x480
../slang/cnn_320/cnn_320.m3u8?bitrate=768000&channel=cnn_320&gp_id=

#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=512000,RESOLUTION=640x360
../slang/cnn_160/cnn_160.m3u8?bitrate=512000&channel=cnn_160&gp_id=

```
## FOR IPTV PLAYBACK
### Android
- Install [NS Player](https://play.google.com/store/apps/details?id=com.genuine.leone)
- Add new Playlist with [this](https://raw.githubusercontent.com/Yeadee/Toffee/main/toffee_channel_data.json) link as URL.

## NOTES

- This Readme documentation is made in resemblance with the docs of the famous Toffee repo by [Byte-Capsule](https://github.com/byte-capsule).
- This script is for educational purposes only. Do not use it for any illegal activities. If the code affects the revenue of the IPTV owners, please let me know and I will delete it.
- Please give me proper credit if you share this content. Otherwise, I will take it down.
- Due to geo-restriction, the contents are only available in Bangladesh.

## Support

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/yeadee)

## QUESTIONS

Questions are welcome at [https://github.com/Yeadee/Toffee/discussions](https://github.com/Yeadee/Toffee/discussions).
This repo is also open for discussion.

## Find Me

<div>
  <a href="https://x.com/i3pranto" target="_blank">
    <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/twitter/default.svg" width="52" height="40" alt="twitter logo"  />
  </a>
  <a href="https://t.me/pranto_bhai" target="_blank">
    <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/telegram/default.svg" width="52" height="40" alt="telegram logo"  />
  </a>
</div>

![](https://api.visitorbadge.io/api/VisitorHit?user=Yeadee&repo=Toffee&countColor=%237B1E7A)

