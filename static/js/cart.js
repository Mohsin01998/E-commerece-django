
var btn=document.getElementsByClassName("update-cart");

for (var i=0; i<btn.length; i++) {
btn[i].addEventListener("click",function(){
var productId=this.dataset.product
var action=this.dataset.action
console.log("productId:",productId,'action:',action);
console.log('USER:',user)
if (user=='AnonymousUser'){
    console.log("not logged in")
    }
else{
    updateUserOrder(productId,action)
}
});
}


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
      console.log("data:",data);
      location.reload()
        });
   }



