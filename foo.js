console.log("AYO")

var i="hello";
var j=20;

var f=function(x) {
    var j=30;
    return j+x;
};

var fact=function(n){
    var j=1;
    for(i=1; i<=n; i++){
	j*=i;
    }
    return j;
};

var factR=function(n){
    if(n==0){
	return 1;
    }else{
	return n*fact(n-1);
    }    
};

var addItem=function(text){
    var list= document.getElementById("thelist");
    var newitem= document.createElement("li");
    newitem.innerHTML=text;
    list.appendChild(newitem);
};


var removeItem=function(n){
    var listitems=document.getElementsByTagName('li');
    listitems[n].remove();
};

var red=function(){
    var items=document.getElementsByTagName("li");
    for(var i=0; i<items.length;i++){
	items[i].classList.add('red');
    }
};
