console.log('user.js loaded');

async function main(){
    let contactFormData = localStorage.getItem('Authorization'); // take JWT

    const requestOptions = {
        method: "GET",
        headers: { "Authorization" : `${contactFormData}` }, // put JWT to request options
    };
    
    async function sendRqst(){
        const response = await fetch('/checkuser', requestOptions); // send request
        // const data = await response.json();
        console.log('Request received');
        return response.status;
    }
    
    if (await sendRqst() >= 400){
        document.getElementById('condition').innerText = 'False';
    } else {
        document.getElementById('condition').innerText = 'True';
    }
}

main()