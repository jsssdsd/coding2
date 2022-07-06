


// let Lid_N1 = document.getElementById("name").value;


let tutol_diva =document.getElementById("tutol_div1")
let tutol_divb =document.getElementById("tutol_div2")
let tutol_divc =document.getElementById("tutol_div3")


let next = document.getElementById("Lbutton1")
let bef = document.getElementById("Lbutton2")


let i0= document.getElementById("i0");
let i1= document.getElementById("i1");
let i2=document.getElementById("i2");
let i3=document.getElementById("i3");
let i4=document.getElementById("i4");
let i5=document.getElementById("i5");
let i6=document.getElementById("i6");
let i7=document.getElementById("i7");
let i8=document.getElementById("i8");
let i9=document.getElementById("i9");


// let nE= addEventListener('click',tutorN);
// let bE= addEventListener('click',tutorB);
next.addEventListener('click',tutorN);
bef.addEventListener('click',tutorB);

let c=0;
function tutorN(){
    console.log(i1)
    c+=1
    console.log(c)
    // if (c==0)
    // {
    //     i0.style.display='block'
    // }
    if (c==1)
    {
        i1.style.display='block'
    }
    else if (c==2)
    {
        i2.style.display='block'
        i1.style.display='none'
    }
    else if (c==3)
    {
        i3.style.display='block'
        i2.style.display='none'
    }
    else if (c==4)
    {
        i4.style.display='block'
        i3.style.display='none'
    }
    else if (c==5)
    {
        i5.style.display='block'
        i4.style.display='none'
    }
    else if (c==6)
    {
        i6.style.display='block'
        i5.style.display='none'
    }
    else if (c==7)
    {
        i7.style.display='block'
        i6.style.display='none'
    }
    else if (c==8)
    {
        i8.style.display='block'
        i7.style.display='none'
    }
    else if (c==9)
    {
        i9.style.display='block'
        i8.style.display='none'
        
    }
    else if (c>9)
    {
        
        c=10
    }
   
    // else if (c==9)
    // {
    // i2.style.display('block')
    // }
}

function tutorB(){
    
    c-=1;
    console.log(i1)
    console.log(c)
    if (c<=0)
    {
        c=0;
    }
    if (c==1)
    {
        i0.style.display='block'
        i1.style.display='none'
        i2.style.display='none'
    }
    else if (c==2)
    {   
        i1.style.display='block'
        i2.style.display='none'
        i3.style.display='none'
    }
    else if (c==3)
    {
        i2.style.display='block'
        i3.style.display='none'
        i4.style.display='none'
    }
    else if (c==4)
    {
        i3.style.display='block'
        i4.style.display='none'
        i5.style.display='none'
    }
    else if (c==5)
    {
        i4.style.display='block'
        i5.style.display='none'
        i6.style.display='none'
    }
    else if (c==6)
    {
        i5.style.display='block'
        i6.style.display='none'
        i7.style.display='none'
    }
    else if (c==7)
    {
        i6.style.display='block'
        i7.style.display='none'
        i8.style.display='none'
    }
    else if (c==8)
    {
        i7.style.display='block'
        i8.style.display='none'
        i9.style.display='none'
    }
    else if (c==9)
    {
        i8.style.display='block'
        i9.style.display='none'
       
    }
    else if (c>9)
    {
        i8.style.display='none'
        i9.style.display='none'
        c=9
    }
    // else if (c==9)
    // {
    // i2.style.display('block')
    // }
    
}



// let Lbt_0 =document.getElementById("Lbutton");

// let Lbt_0 =document.getElementById("Lbutton");