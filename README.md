# twitch-clip-archive
단일 스트리머용 트위치 클립 백엔드리스 아카이빙 웹 시스템<br/>
(twitch clip archiving backendless web system for a single streamer)

# 사용방법
해당 tools 내에 들어있는 코드를 순서대로 실행하면 됩니다.
- `1.make_twitch_clips_origin_json.py` 를 실행하여 `origin.json`을 만드세요. (스크랩에 대한 이슈가 있어 소스코드 제외)
- `2.download_origin_video_and_thumbnail.py`를 실행하여 동영상과 썸네일을 다운 받으세요. (네트워크 문제로 인해 여러번 수행해야할 수 있습니다)
- `3.origin_json_convert_to_local_json.py`를 실행하여 `origin.json`을 `clips.json`으로 변환하세요.
- 이제 `index.html`로 직접 아카이브된 클립들을 확인할 수 있습니다.

# 동작화면
![sample](sample.gif)
> 개인정보 노출을 최소화하기 위해 임의로 모자이크 처리하였습니다. 양해 바랍니다.

# 안내사항
해당 시스템은 별도로 동영상 및 썸네일을 다운받지 않고도 `origin.json`을 `clips.json`으로 파일이름만 변경하여 활용하실 수 있습니다.<br/>
다만, 썸네일과 동영상 호출에서 과도한 네트워크 트래픽 발생으로 인하여 차단 당하실 수 있으니 주의 바랍니다.