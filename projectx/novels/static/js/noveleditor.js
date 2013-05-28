function content(){return $("#novel_content").data("sceditor").val();}

$(document).ready(function(){
  $('#novel_content').sceditor({
    toolbar: "bold,italic,underline,strike,subscript,superscript|left,center,right,justify|" +
             "font,size,color,quote,removeformat|cut,copy,paste,pastetext|bulletlist,orderedlist|" +
             "image,video,tableau,email,link,unlink|print,maximize"
  }); 
});

