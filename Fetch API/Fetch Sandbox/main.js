document.getElementById('getText').addEventListener('click', getText)
document.getElementById('getUsers').addEventListener('click', getUsers)
document.getElementById('getPosts').addEventListener('click', getPosts)
document.getElementById('addPost').addEventListener('click', addPost)

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
        })
        .catch(err=>console.log(err))
}


// from jsonplaceholder -> Routes -> /posts
function getPosts() {
    fetch('https://jsonplaceholder.typicode.com/posts')
        .then(response => response.json())

        .then(data => {
            let output = '<h2>Posts</h2>'
            data.forEach(function(posts) {
                output += ` 
                <div>
                    <h3>${posts.title}</h3>
                    <p>${posts.body}</p>
                </div>
                `;
            });
            document.getElementById('output').innerHTML = output;
        })
        .catch(err => console.log(err))
}



function addPost(e) {
    e.preventDefault(); // since it's form, prevent it from submitting to a file

    let title = document.getElementById('title').value
    let body = document.getElementById('body').value

    fetch('https://jsonplaceholder.typicode.com/posts', {
        method: 'POST',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-type': 'application/json'
        },
        body:JSON.stringify({title:title, body:body})
    })
    .then(res=>res.json())
    .then(data=>console.log(data))
}