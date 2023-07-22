//////////////////////////////
// SCRIPT TO INCEJT CODE
//////////////////////////////


// Declare Variables
// [['2023-07-27', '2023-08-31', 'cfc'], ['2023-09-5', '2023-09-30', 'cfc'], ['2023-10-01', '2024-01-07', 'fcc']]
let el1;
var i;


// main code
document.onreadystatechange = () => {
    if (document.readyState === 'complete') {

        // Set up 
        chrome.storage.sync.set({"inputs": [['2023-07-27', '2023-08-31', 'cfc'], ['2023-09-5', '2023-09-30', 'cfc'], ['2023-10-01', '2024-01-07', 'fcc']]});

        // read all Dates on start
        paint();


        // read all Dates on change cookies
        chrome.storage.onChanged.addListener((changes, area) => {
            if (area == "sync") {
                paint();
            }
        })
    }
};


/////////////////////////////////////
// USEFULL FUNCTIONS
/////////////////////////////////////

function DTK(date) {
    date = new Date(date)
    const y = date.getFullYear() - 1970;
    const m = date.getMonth()+1;   
    const d = date.getDate();
    return (y<<9) + (m<<5) + d;
}

function paint() {
    chrome.storage.sync.get(["inputs"], (result) => {
        result["inputs"].forEach((element) => {
            for(i = DTK(element[0]); i <= DTK(element[1]); i++) {
                try { 
                    el1 = document.querySelector(`[data-datekey="${i}"]`)
                    el1.style.backgroundColor = "#" + element[2]
                } catch {}
            }
        })
    })
}