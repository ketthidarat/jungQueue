function tick(){
    var timeDisplay=document.getElementById("time");
    var min=Math.floor(mySeconds/60);
    var sec=mySeconds-(min*60);
    if (sec < 10) {
    sec="0"+sec;
    }
    var message=min.toString()+":"+sec;
    timeDisplay.innerHTML=message;
    if(mySeconds===0){
    alert("Done");
    clearInterval(intervalHandle);
    resetPage();
    }
    mySeconds--;
    }