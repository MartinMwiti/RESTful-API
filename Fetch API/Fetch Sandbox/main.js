document.getElementById('getText').addEventListener('click', getText)
document.getElementById('getUsers').addEventListener('click', getUsers)

function getText() {
    fetch('sample.txt') // fetch returns a promise
    .then((response)=>
        // console.log(response.text()) // console.log(response.json()) - for json file
        response.text()
    )
    // .then((data)=>
    //     console.log(data) // get the actual text data in the console
    // )
    .then((data)=>
        document.getElementById('output').innerHTML= data // print the text data into the html
    )
    .catch((err)=>console.log(err))
}


function getUsers() {
    fetch('users.json') 
        .then(response=>response.json())

        .then(data =>{
            let output = '<h2>Users</h2>'
            data.forEach(function(user){
                output += ` 
                <ul>
                <li>ID: ${user.id}</li>
                <li>Name: ${user.name}</li>
                <li>Email: ${user.email}</li>
                </ul>
                `;
            });
            document.getElementById('output').innerHTML=output;
        });

}