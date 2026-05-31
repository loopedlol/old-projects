function submitName(){
    var name = document.getElementById("name").value;
    fetch(`https://api.agify.io/?name=${name}`).then(function(response){
        return response.json()
    }).then(function(data){
        document.getElementById("namedisplay").innerHTML = "Name: " + data.name
        document.getElementById("agedisplay").innerHTML = "Age: " + data.age
        document.getElementById("countdisplay").innerHTML = "Count: " + data.count
    })
}