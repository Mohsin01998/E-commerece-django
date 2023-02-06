console.log('Hello world')

var updateBtns=document.getElementsByClassName('update-cart')

for (i=0; i<updateBtns.length; i++) {
updateBtns[i].addEventListner('click', function(){
var productId=this.dataset.product
var action=this.dataset.action
console.log('productId:',productId,'Action:',action)
})
}