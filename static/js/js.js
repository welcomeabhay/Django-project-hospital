function Deletion(){
choice=confirm("Do you want to delete the place?");
return choice;

}


function Validation(){
Psd=document.r_form.psd.value;
Cpsd=document.r_form.cpsd.value;
if(Psd==Cpsd){
   return true
}
else{
   alert("Password and confirm password must be same.")
return false
}

}