function countVote(){
    window.location.href = "/final";
}

const interval = setInterval(async () => {
    const res = await fetch('/count');
    const data = await res.json();
    console.log(data.count);
    for (var node of document.getElementsByClassName("btn")) {
        node.disabled = data.count !== 1;
    }
  }, 2000);