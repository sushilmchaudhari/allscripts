hsh = {
  "srcBucket": "msri-video-tube-source-bbwudbcpp32z",
  "abrBucket": "msri-video-tube-abrdestination-zn7vukv4q8zc",
  "mp4Bucket": "msri-video-tube-mp4destination-1wow7v8o7pk18",
  "workflowStatus": "ingest",
  "startTime": "2018-10-22 07:05.5",
  "srcVideo": "860_24384_5361_small_video4_1080p.mp4",
  "mp4": [
    1080,
    720,
    360
  ],
  "hls": [
    1080,
    720,
    540,
    360,
    270
  ],
  "dash": [
    1080,
    720,
    540,
    360,
    270
  ],
  "frameCapture": true,
  "srcMediainfo": "{\n  \"container\": {\n    \"format\": \"MPEG-4\",\n    \"mimeType\": \"video/mp4\",\n    \"fileSize\": 6586323,\n    \"duration\": 5547,\n    \"totalBitrate\": 9498933\n  },\n  \"video\": [\n    {\n      \"codec\": \"AVC\",\n      \"width\": 1920,\n      \"height\": 1080,\n      \"profile\": \"Main@L5\",\n      \"bitrate\": 9378859,\n      \"duration\": 5520,\n      \"framerate\": 25,\n      \"frameCount\": 138,\n      \"scanType\": \"Progressive\"\n    }\n  ],\n  \"audio\": [\n    {\n      \"codec\": \"AAC\",\n      \"profile\": \"LC\",\n      \"bitrate\": 160000,\n      \"bitrateMode\": \"VBR\",\n      \"duration\": 5547,\n      \"language\": \"en\",\n      \"channels\": 2,\n      \"frameCount\": 260,\n      \"samplingRate\": 48000,\n      \"samplePerFrame\": 1024\n    }\n  ],\n  \"text\": []\n}",
  "guid": "e0ae1779-8485-4f1a-8d76-abc952c85394"
}

//var body = hsh.srcMediainfo;
//console.log (body)
//console.log(JSON.stringify(body, null, 2));
//var temp = `${hsh.srcMediainfo}`;
//body_hsh = JSON.parse(JSON.stringify(body));
body_hsh = JSON.parse(`${hsh.srcMediainfo}`);
//console.log(body_hsh);
console.log(body_hsh.container.mimeType);
//console.log(JSON.parse(temp).hlsUrl);
