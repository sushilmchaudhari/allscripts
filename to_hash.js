'use strict';

let event = {
    "ecodeJobId": "1537507216450-y97ha6",
    "workflowStatus": "processing",
    "origVideoName": "72a4bbe2-38d4-4683-9137-4719b336b80c_View_From_A_Blue_Moon_Trailer-576p.mp4",
    "frameCapture": true,
    "frameWdith": 1280,
    "mp4Bucket": "msri-video-tube-mp4destination-1wow7v8o7pk18",
    "abrBucket": "msri-video-tube-abrdestination-zn7vukv4q8zc",
    "hls": [
        540,
        360,
        270
    ],
    "dash": [
        540,
        360,
        270
    ],
    "srcMediainfo": "{\n  \"container\": {\n    \"format\": \"MPEG-4\",\n    \"mimeType\": \"video/mp4\",\n    \"fileSize\": 49900386,\n    \"duration\": 183126,\n    \"totalBitrate\": 2179937\n  },\n  \"video\": [\n    {\n      \"codec\": \"AVC\",\n      \"width\": 720,\n      \"height\": 576,\n      \"profile\": \"Main@L3.1\",\n      \"bitrate\": 2000000,\n      \"duration\": 183058,\n      \"framerate\": 23.976,\n      \"frameCount\": 4389,\n      \"scanType\": \"Progressive\"\n    }\n  ],\n  \"audio\": [\n    {\n      \"codec\": \"AAC\",\n      \"profile\": \"LC\",\n      \"bitrate\": 173023,\n      \"bitrateMode\": \"VBR\",\n      \"duration\": 183126,\n      \"language\": \"en\",\n      \"channels\": 2,\n      \"frameCount\": 8584,\n      \"samplingRate\": 48000,\n      \"samplePerFrame\": 1024\n    }\n  ],\n  \"text\": []\n}",
    "startTime": "2018-09-21 05:20.1",
    "mp4": [
        1080,
        720,
        360
    ],
    "guid": "994ab788-65dc-4367-a082-1ad6f5d8c852",
    "frameHeight": 720,
    "srcVideo": "72a4bbe2-38d4-4683-9137-4719b336b80c_View_From_A_Blue_Moon_Trailer-576p.mp4",
    "srcBucket": "msri-video-tube-source-bbwudbcpp32z",
    "srcHeight": 576,
    "newVideoName": "72a4bbe2-38d4-4683-9137-4719b336b80c_View_From_A_Blue_Moon_Trailer-576p.mp4",
    "srcWidth": 720
};

let posBase = event.srcVideo.split(".").slice(0, -1);

let RegionName = 'us-west-1';

console.log("Poster Base: ", posBase);

if (event.frameCapture) {
    
    for (let i = 0;  i < 20; i++) { 
	Number.prototype.pad = function(size) {
 		 var s = String(this);
  		while (s.length < (size || 2)) {s = "0" + s;}
  		return s;
	}
	
	console.log('Number are: ', (i).pad(7));
    	event.posterUrl = {
		i: 'https://s3-' + RegionName + '.amazonaws.com/' + event.mp4Bucket + '/' + event.guid + /thumbnails/ + posBase + '_mp4_tumb.' + 0000001 + '.jpg'
	}
    }
    console.log('Poster URLS:', JSON.stringify(event.posterUrl, null, 2));
}
