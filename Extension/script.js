//////////////////////////////
// SCRIPT IN POP UP
//////////////////////////////

document.onreadystatechange = () => {
  if (document.readyState === 'complete') {

    //Add a Date
    document.getElementById("submit").addEventListener("click", (e) => {
      chrome.storage.sync.get(["inputs"], (result) => {
        chrome.storage.sync.set({"inputs": 
        result["inputs"].concat([[
          document.getElementById("inp1").value, 
          document.getElementById("inp2").value, 
          document.getElementById("inp3").value
      ]])})
    })


    // Show existing Dates
    showOld()

    // Export File
    document.getElementById("export").addEventListener("click", (e) => {
      chrome.storage.sync.get("inputs", (result) => {
        download("colored_calender.txt", result["inputs"])
      })
    })


    // Import File
    // document.getElementById("import").addEventListener("click", (e) => {
    //   chrome.storage.sync.set({"inputs": [["2023-07-24", "2023-07-27", "ccf"]]})
    //   console.log(document.getElementById("inp4").target.files)
    //   const reader = new FileReader();
      
    //     chrome.storage.sync.set({"inputs":
    //       document.getElementById("inp4").target.files[0]
    // })
      
})}}



//////////////////////////////
// USEFULL FUNCTIONS
//////////////////////////////

function download(filename, text) {
  var element = document.createElement('a');
  element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
  element.setAttribute('download', filename);

  element.style.display = 'none';
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);
}

function showOld() {
  old = document.getElementById("old")
  chrome.storage.sync.get(["inputs"], (result) => {
    for (i = 0; i < result["inputs"].length; i++) {
      old.innerHTML = "<div> " + result["inputs"][i] + "</div>"
    }
  })
}

