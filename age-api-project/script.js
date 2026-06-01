function submitName(){
    var name = document.getElementById("name").value;
    var encodedName = encodeURIComponent(name);
    fetch(`https://api.agify.io/?name=${encodedName}`).then(function(response){
        return response.json()
    }).then(function(data){
        document.getElementById("namedisplay").innerHTML = "Name: " + data.name
        document.getElementById("agedisplay").innerHTML = "Age: " + data.age
        document.getElementById("countdisplay").innerHTML = "Count: " + data.count
    }).catch(function(){
        document.getElementById("result").innerHTML = "Could not get age data."
    })
}
