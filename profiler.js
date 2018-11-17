'use strict';

  //check the defined presets (resolution) are lessthan or equal to the source
  // height (resolution)

  let event = {};
  let hls = [1080, 720, 540, 360, 270];
  let dash = [1080, 720, 540, 360, 270];
  let mp4 = [720];
  let srcHeight = 240;
  let srcWidth = 320;


  function presetCheck(height,presets) {
//    const newPresets = new Set([270]);
    let newPresets = [];
    presets.forEach(function(p) {
      if (p <= height || p === 270) {
        newPresets.push(p);
//        newPresets.add(p);
      } else {
        console.log(p+' removed from presets as the source is only', height,'p');
      }
    });
    return newPresets;
  }

  if (hls) {
    event.hls = presetCheck(srcHeight,hls);
  }
  if (mp4) {
    event.mp4 = presetCheck(srcHeight,mp4);
  }
  if (dash) {
    event.dash = presetCheck(srcHeight,dash);
  }

  console.log('Dash ->', event.dash);
  console.log('Hls ->', event.hls);
  console.log('mp4 ->', event.mp4);

