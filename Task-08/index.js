let playSound = function(soundId) {
    let audio = document.getElementById(soundId);
    audio.currentTime = 0; // Reset the audio to the beginning
    audio.play();
  };
  
  let playw = function() {
    playSound("audiow");
  };
  let playa = function() {
    playSound("audioa");
  };
  let plays = function() {
    playSound("audios");
  };
  let playd = function() {
    playSound("audiod");
  };
  let playj = function() {
    playSound("audioj");
  };
  let playk = function() {
    playSound("audiok");
  };
  let playl = function() {
    playSound("audiol");
  };
  
document.addEventListener("keydown", function(event) {
  if (event.key === "w") {
    playw();
  } else if (event.key === "a") {
    playa();
  } else if (event.key === "s") {
    plays();
  } else if (event.key === "d") {
    playd();
  } else if (event.key === "j") {
    playj();
  } else if (event.key === "k") {
    playk();
  } else if (event.key === "l") {
    playl();
  }
});