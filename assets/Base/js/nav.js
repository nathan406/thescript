document.addEventListener("DOMContentLoaded", function() {
    var nav = document.getElementById("site-header");
    var prevScrollPos = window.pageYOffset;
  
    window.onscroll = function() {
      var currentScrollPos = window.pageYOffset;
      var transparency = currentScrollPos / 1000; // You can adjust the division value as needed
  
      if (transparency > 1) {
        transparency = 1;
      }
  
      nav.style.backgroundColor = "rgba(128, 0, 0, " + transparency + ")";
      prevScrollPos = currentScrollPos;
    };
  });






  