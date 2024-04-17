

const darkmode = document.querySelector('.dark-mode');






darkmode.addEventListener('click', () =>{
  document.body.classList.toggle('dark-mode-variables');
  darkmode.querySelector('span:nth-child(1)').classList.toggle('active');
  darkmode.querySelector('span:nth-child(2)').classList.toggle('active');
})


function myFun() {
  document.getElementById("myDropdown").classList.toggle("show");
}
function filterFun() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  div = document.getElementById("myDropdown");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}


function myFunction() {
  
  document.getElementById("myDropdown1").classList.toggle("show");
}
function filterFunction() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("myInput1");
  filter = input.value.toUpperCase();
  div = document.getElementById("myDropdown1");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}





