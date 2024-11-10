document.getElementById("addtask").addEventListener("click", () => {

    let newtask = document.getElementById("newtask").value;

    const tasklist = document.getElementById("tasks");
    const theli = document.createElement("li");

    theli.textContent = newtask;
    theli.style.color = "white";
    tasklist.appendChild(theli);    

    theli.addEventListener("click", () => {
        theli.style.textDecoration = theli.style.textDecoration === "line-through" ? "none": "line-through";
        theli.style.color = theli.style.color === "red" ? "white": "red";   
    });

    
});


const checkbox = document.getElementById("filter1");

checkbox.addEventListener("change", () => {
    const listItems = document.getElementById("tasks").getElementsByTagName("li");
    Array.from(listItems).forEach(item => {
        if (checkbox.checked && item.style.color === "red") {
            item.style.display = "none";
        } else { 
            item.style.display = "block";
        }
    });
});

const checkbox2 = document.getElementById("filter2");

checkbox2.addEventListener("change", () => {
    const listItems = document.getElementById("tasks").getElementsByTagName("li");
    Array.from(listItems).forEach(item => {
        if (checkbox2.checked && item.style.color === "white") {
            item.style.display = "none";
        } else { 
            item.style.display = "block";
        }
    });
});