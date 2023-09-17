console.log("requests script");

function getClientRequests() {

    
    fetch("http://localhost:5000/requestclient")
    .then(requestclient => requestclient.json())
    .then(requestclient => {
        console.log(requestclient);
        
        const requestsTag = document.getElementById("requestclient");
        requestsTag.innerText = `${JSON.stringify(requestclient, null, "two spaces")}`
    })
    .catch(e => console.error(e));


}
//getClientRequests();


// look up how to do post request using html and javascript and fetch
// look up javascript promises, then, catch