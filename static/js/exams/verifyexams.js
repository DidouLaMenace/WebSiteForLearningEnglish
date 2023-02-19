let sendButton = document.getElementById("btn-restart");
var listofuseranswer = [];

function getAllAnswer(){
    var inputs = document.querySelectorAll("input");
    for (var i = 0; i < inputs.length; i++) {
        listofuseranswer.push(inputs[i].value);
    }
    console.log(voc_response_to_translate_frenchexams);
    console.log(voc_response_to_translate_englishexams);
    verify_translate_in_english(listofuseranswer[lenliste],voc_response_to_translate_englishexams);
}

function verify_translate_in_english(list_answer, list_expect_answer) {
    var listverify = []
    if (list_answer.length !== list_expect_answer.length) {
      return false;
    }
    for (var i = 0; i < list_answer.length; i++) {
      if (list_answer[i] !== list_expect_answer[i]) {
        listverify.push("false");
      }
      else {
        listverify.push("true");
      }
    }
    return listverify;
}

function verify_translate_in_french(list_answer, list_expect_answer) {
    var listverify = []
    if (list_answer.length !== list_expect_answer.length) {
      return false;
    }
    for (var i = 0; i < list1.length; i++) {
      if (list_answer[i] !== list_expect_answer[i]) {
        listverify.push("false");
      }
      else {
        listverify.push("true");
      }
    }
    return listverify;
}
  