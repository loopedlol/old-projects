function factorial() {
    fetch("/factorial/" + $("#factorial").val()).then((response) => {
            return response.text();
        }).then((data) => {
            console.log(data);
            $("#result").html(data);
        })
}

function fibonacci() {
    fetch("/fibonacci/" + $("#fibonacci").val()).then((response) => {
            return response.text();
        }).then((data) => {
            console.log(data);
            $("#result").html(data);
        })
}

function average() {
    fetch("/average/" + $("#avg1").val() + "/" + $("#avg2").val()).then((response) => {
            return response.text();
        }).then((data) => {
            console.log(data);
            $("#result").html(data);
        })
}
