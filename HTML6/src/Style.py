center_css = """.center {
  display: flex;
  justify-content: center;
  align-items: center;
}
"""
center_vertical_css = """.vertical {
  display: flex;
  justify-content: left;
  align-items: center;
}
"""
center_horizontal_css = """.horizontal {
  display: flex;
  justify-content: center;
  align-items: start;
}
"""

# ------------------------------- MAIN --------------------------------
fullscreen_css = """.fullscreen {
    width: 100vw;
    height: 100hw;
}
"""

body_css = """body {
    padding: 0;
    margin: 0;
    font-family: 'Roboto Mono';
}
"""
roboto_html = "\t\t<link href='https://fonts.googleapis.com/css?family=Roboto Mono' rel='stylesheet'>\n\t\t<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'>\n"


# ----------------- ITEMS -------------------
to_the_top_js = """let mybuttons = document.getElementsByClassName("to_the_top");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    for (let i = 0; i < mybuttons.length; i++) {
        let element = mybuttons[i];
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            element.style.display = "block";
        } else {
            element.style.display = "none";
        }
    }
}

// When the user clicks on the button, scroll to the top of the document
function to_the_top() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}"""
to_the_top_css = """#myBtn {
  display: none;
  position: fixed;
  bottom: 20px;
  right: 30px;
  z-index: 99;
}
"""

for_js = """"""

code_highlight_header = """\t\t<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/default.min.css">
\t\t<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
\t\t<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/go.min.js"></script>
\t\t<script>hljs.highlightAll();</script>
"""
parallax_css = """.parallax {
  /* Full height */
  height: 100%; 

  /* Create the parallax scrolling effect */
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
"""

dropdown_hover_css = """.dropbtn {
  padding: 16px;
  font-size: 16px;
  border: none;
  cursor: pointer;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #ddd;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content item {
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content item:hover {background-color: #aaa; cursor: pointer;}

.dropdown:hover .dropdown-content {
  display: block;
}

.dropdown:hover .dropbtn {
  background-color: #3e8e41;
}
"""
dropdown_click_css = """.dropbtn {
  color: white;
  padding: 16px;
  font-size: 16px;
  border: none;
  cursor: pointer;
}

.dropbtn:hover, .dropbtn:focus {
  background-color: #2980B9;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #ddd;
  min-width: 160px;
  overflow: auto;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown a:hover {background-color: #aaa;}

.show {display: block;}
"""
dropdown_click_js = """function dorpdown_click() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
"""
slideshow_js ="""
function plusSlides(n, no) {
  showSlides(slideIndex[no] += n, no);
}

function showSlides(n, no) {
  let i;
  let x = document.getElementsByClassName(slideId[no]);
  if (n > x.length) {slideIndex[no] = 1}    
  if (n < 1) {slideIndex[no] = x.length}
  for (i = 0; i < x.length; i++) {
     x[i].style.display = "none";  
  }
  x[slideIndex[no]-1].style.display = "block";  
}
"""

slideshow_css = """* {box-sizing: border-box}
.slideshow-container img {vertical-align: middle;max-width: 1000px;}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Next & previous buttons */
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  padding: 16px;
  margin-top: -22px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
}

/* Position the "next button" to the right */
.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

/* On hover, add a grey background color */
.prev:hover, .next:hover {
  background-color: #f1f1f1;
  color: black;
}
"""

split_css = """div {
    box-sizing: border-box; /* Include padding and border in the element's total width and height */
    padding: 0;
    margin: 0;
    min-height: 20px;
    height: 100%;
}
.outer-container:not(.outer-container .outer-container) {
    display: flex;
    align-items: stretch; /* Make the outer container stretch to the full height of its children */
}
"""


img_css = """.modal-target {
  width: 300px;
  border-radius: 5px;
  cursor: pointer;
  transition: 0.3s;
}

.modal-target:hover {opacity: 0.7;}

/* The Modal (background) */
.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  padding-top: 100px; /* Location of the box */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.8); /* Black w/ opacity */
}

/* Modal Content (image) */
.modal-content {
  margin: auto;
  display: block;
  width: 80%;
  opacity: 1 !important;
  max-width: 1200px;
}

/* Caption of Modal Image */
.modal-caption {
  margin: auto;
  display: block;
  width: 80%;
  max-width: 1200px;
  text-align: center;
  color: white;
  font-weight: 700;
  font-size: 1em;
  margin-top: 32px;
}

/* Add Animation */
.modal-content, .modal-caption {  
  -webkit-animation-name: zoom;
  -webkit-animation-duration: 0.6s;
  animation-name: zoom;
  animation-duration: 0.6s;
}

@-webkit-keyframes zoom {
  from {-webkit-atransform:scale(0)} 
  to {-webkit-transform:scale(1)}
}

@keyframes zoom {
  from {transform:scale(0)} 
  to {transform:scale(1)}
}

/* The Close Button */
.modal-close {
  position: absolute;
  top: 15px;
  right: 35px;
  color: #f1f1f1;
  font-size: 40px;
  font-weight: bold;
  transition: 0.3s;
}

.modal-close:hover,
.modal-close:focus {
  color: #bbb;
  text-decoration: none;
  cursor: pointer;
}
"""
img_js = """// Modal Setup
var modal = document.getElementById('modal');

var modalClose = document.getElementById('modal-close');
modalClose.addEventListener('click', function() { 
  modal.style.display = "none";
});

// global handler
document.addEventListener('click', function (e) { 
  if (e.target.className.indexOf('modal-target') !== -1) {
      var img = e.target;
      var modalImg = document.getElementById("modal-content");
      var captionText = document.getElementById("modal-caption");
      modal.style.display = "block";
      modalImg.src = img.src;
      captionText.innerHTML = img.alt;
   }
});
"""


known_elements = {
    # ----------------- P -------------------
    "p": [None, """p {
    color: #000;
    padding: 10px;
}
    """, None],


    # ----------------- NAVBAR -------------------
    "navbar": [None, """navbar {
    display: inline-block;
    background-color: #eee;
    width: 100vw;
    margin: 0;
    padding: 0;
}
""", None],


    # ------------------- BUTTON -----------------
    "button": [None, """button:hover {
    background-color: #3e8e41;
}
button {
      background-color: #04AA6D; /* Green */
      border: none;
      color: Black;
      padding: 15px 32px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      cursor: pointer;
      margin-left: 0;
}
navbar button {
	background-color: #ddd;
}
""", None],

	# ------------------- DROPDOWN -----------------
	"to_the_top": [None, to_the_top_css, to_the_top_js],
    

    # ---------------- A --------------------
    "a": [None, """a {
    text-decoration: none;
    color: #000;
    cursor: pointer;
}
navbar a:hover {
    background-color: #aaa;
}
navbar a {
    background-color: #ddd;
    padding: 15px 32px;
    margin: 0;
}
""", None],

	# ------------------- DROPDOWN -----------------
  "center": [None, center_css, None],


    # ------------------ IMG ------------------
    "img_modem": ["""<div id="modal" class="modal">
  <span id="modal-close" class="modal-close">&times;</span>
  <img id="modal-content" class="modal-content">
  <div id="modal-caption" class="modal-caption"></div>
</div>
""", img_css, img_js],

	# ------------------- H1 -----------------
    "h1": [None, """h1 {padding: 10px;
      }""", None], 
      
	# ------------------- DROPDOWN -----------------
	"dropdown_hover": [None, dropdown_hover_css, None],
	"dropdown_click": [None, dropdown_click_css, dropdown_click_js],
    
	# -------------------CENTER -----------------
	"center_vertical": [None, center_vertical_css, None],
	"center_horizontal": [None, center_horizontal_css, None],

    # ------------------- Inputs -----------------
  "input": [None, """input:type[type="toggle"] {
        cursor: pointer;
        background-color: #ccc;
        padding: 10px;
    }
    """, None],

    # ------------------- Parallax -----------------
    "parallax": [None, parallax_css, None],

    # ------------------- Slideshow -----------------
    "slideshow": [None, slideshow_css, slideshow_js],

    # ------------------- Split -----------------
    "split": [None, split_css, None],
}
