function speakFrench(text) {
    const synth = window.speechSynthesis;
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.onerror = (event) => {
        console.error('Speech synthesis error:', event.error);
    };
    //French voice : 38
    utterance.voice = synth.getVoices()[38];
    utterance.rate = 1; 
    utterance.pitch = 1;
    utterance.volume = 1;
    synth.speak(utterance);
}

function speakEnglish(text) {
    const synth = window.speechSynthesis;
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.onerror = (event) => {
        console.error('Speech synthesis error:', event.error);
    };
    //English voice : 102
    utterance.voice = synth.getVoices()[102];
    utterance.rate = 1; 
    utterance.pitch = 1;
    utterance.volume = 1;
    synth.speak(utterance);
}