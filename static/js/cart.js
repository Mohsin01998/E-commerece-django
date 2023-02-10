console.log('Hello world')

function getToken(name) {
let cookieValue = null;
if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
        }
    }
}
return cookieValue;
}
var csrftoken = getToken('csrftoken');


var btn=document.getElementsByClassName("update-cart");


for (var i=0; i<btn.length; i++) {
btn[i].addEventListener("click",function(){
var productId=this.dataset.product
var action=this.dataset.action
console.log("productId:",productId,'action:',action);
console.log('USER:',user)
if (user=='AnonymousUser'){
console.log('User is not authenticated')}
else{
    updateUserOrder(productId,action)
}
});
}

//console.log(csrftoken)
function updateUserOrder(productId,action){
    console.log('User is authenticated, sending data...')
    var url='update_item'
    fetch(url, {
      method: "POST",
//      credentials: "same-origin",
      headers: {
//        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": csrftoken,
        },
      body: JSON.stringify({"productId":productId,'action':action})
        })
    .then(response => response.json())
    .then(data => {
      console.log(data);
      location.reload()
        });
   }







