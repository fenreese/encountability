console.log("getfriends script");

function getFriends() {

    
    fetch("http://localhost:5000/friends")
    .then(friends => friends.json())
    .then(friends => {
        console.log(friends);
        
        const friendsTag = document.getElementById("friends");
        friendsTag.innerText = `${JSON.stringify(friends)}`
    })
    .catch(e => console.error(e));


}
//getFriends();


// look up how to do post request using html and javascript and fetch
// look up javascript promises, then, catch
