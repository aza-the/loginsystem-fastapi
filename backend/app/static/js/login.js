console.log("Log loaded");

document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById("form-login").addEventListener("submit", async function(e) {
        e.preventDefault() // Cancel the default action
        await submitData();
    });
});

async function submitData(){
    const form = document.getElementById('form-login');
    const formData = new FormData(form);

    const requestOptions = {
        method: "POST",
        headers: { "Content-Type" : "application/x-www-form-urlencoded" },
        body: JSON.stringify(
            `grant_type=&username=${formData.get('username')}&password=${formData.get('password')}&scope=&client_id=&client_secret=`
        )
    }

    let response = await fetch("/login", requestOptions);
    const data = await response.json();

    if(!response.ok) {
        console.log('Error');
    } else {
        localStorage.setItem("Authorization", `Bearer ${data.access_token}`);
        console.log('Access token saved');
    }
}