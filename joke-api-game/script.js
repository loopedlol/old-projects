var currentjokedata = null;

function getJoke(){
    var type = document.getElementById("type").value;
    var encodedType = encodeURIComponent(type);
    fetch(`https://official-joke-api.appspot.com/jokes/${encodedType}/random`).then(function(response){
        return response.json()
    }).then(function(data){
        if (!data || !data[0]) {
            document.getElementById("jokeSetup").innerHTML = "No joke found for that type.";
            currentjokedata = null;
            return;
        }
        currentjokedata = data;
        document.getElementById("jokeSetup").innerHTML = data[0].setup;
        document.getElementById("punchlineSpace").innerHTML = "";
    }).catch(function(){
        document.getElementById("jokeSetup").innerHTML = "Could not get a joke.";
        currentjokedata = null;
    })
}

function getPunchline(){
    if (!currentjokedata || !currentjokedata[0]) {
        document.getElementById("punchlineSpace").innerHTML = "Get a joke first.";
        return;
    }
    document.getElementById("punchlineSpace").innerHTML = currentjokedata[0].punchline;
}
