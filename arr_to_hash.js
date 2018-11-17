'use strict';
const AWS = require('aws-sdk');

const s3 = new AWS.S3();

const RegionName = 'us-west-1';

let event = {
    "ecodeJobId": "1536587360614-3nbx13",
    "workflowStatus": "processing",
    "origVideoName": "cf-test-dolby3.mp4",
    "frameCapture": false,
    "mp4Bucket": "cf-mflex-5-mp4destination-1plbg3r3s7hnv",
    "abrBucket": "cf-mflex-5-abrdestination-wwqnwz9tfyjm",
    "hls": [
        360,
        270
    ],
    "dash": [
        360,
        270
    ],
    "srcMediainfo": "{\n  \"container\": {\n    \"format\": \"MPEG-4\",\n    \"mimeType\": \"video/mp4\",\n    \"fileSize\": 3155400,\n    \"duration\": 38072,\n    \"totalBitrate\": 663038\n  },\n  \"video\": [\n    {\n      \"codec\": \"AVC\",\n      \"width\": 720,\n      \"height\": 480,\n      \"profile\": \"High@L3\",\n      \"bitrate\": 313322,\n      \"duration\": 38072,\n      \"framerate\": 29.97,\n      \"frameCount\": 1141,\n      \"scanType\": \"Progressive\"\n    }\n  ],\n  \"audio\": [\n    {\n      \"codec\": \"AAC\",\n      \"profile\": \"LC\",\n      \"bitrate\": 341351,\n      \"bitrateMode\": \"CBR\",\n      \"duration\": 38006,\n      \"channels\": 2,\n      \"frameCount\": 1782,\n      \"samplingRate\": 48000,\n      \"samplePerFrame\": 1024\n    }\n  ],\n  \"text\": []\n}",
    "startTime": "2018-09-10 13:49.7",
    "mp4": [
        1080,
        720,
        360
    ],
    "guid": "0b08b84a-a1ef-424a-b079-d033430616b1",
    "srcVideo": "915_24502_5344_cf-test-dolby3.mp4",
    "srcBucket": "cf-mflex-5-source-13s87az2nuf6p",
    "srcHeight": 480,
    "newVideoName": "915_24502_5344_cf-test-dolby3.mp4",
    "srcWidth": 720
};

let mp4Base = event.guid + '/mp4/' + event.srcVideo.split(".").slice(0, -1).join(".");

/*
var params = {
  Bucket: event.mp4Bucket
};

s3.getBucketLocation(params, function(err, data) {
  if (err) console.log(err, err.stack); // an error occurred
  else     console.log(data);           // successful response
});
*/

if (event.mp4 && event.mp4.length > 0) {
  event.mp4Outputs = {};
  for (let i = event.mp4.length - 1; i >= 0; i--) {
    let key = mp4Base + '_' + event.mp4[i] + 'p.mp4';
    let mp4Url = 'https://s3-' + RegionName + '.amazonaws.com/' + event.mp4Bucket + '/' + key;
    console.log('Mp4 Url is :-> ', mp4Url);
    if (key.includes('360p')) event.mp4Outputs.mp4_360 = key;
    if (key.includes('720p')) event.mp4Outputs.mp4_720 = key; 
    if (key.includes('1080p')) event.mp4Outputs.mp4_1080 = key;
  }
}

console.log('MP4 outputs: ', JSON.stringify(event.mp4Outputs, null, 2));
