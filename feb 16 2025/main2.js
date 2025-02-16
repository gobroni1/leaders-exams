

function showBooks2 (){
    const books = JSON.parse(localStorage.getItem("books")) || [];
    const main2 = document.getElementById("sec-main");


    books.forEach(book => {
       const itemBook = document.createElement("div");
       itemBook.classList.add("item-book") //this is class to stile 

       const forTitle2 = document.createElement("h2");
       forTitle2.textContent = book.title;

       const authore2 = document.createElement("h3");
       authore2.textContent = book.authore;

       const descript2 = document.createElement("p");
       descript2.textContent = book.desc;

       const read2 = document.createElement("p");
       read2.textContent = `status: ${book.read}`; 

       //

       itemBook.appendChild(forTitle2);
       itemBook.appendChild(authore2);
       itemBook.appendChild(descript2);
       main2.appendChild(itemBook);
    });
}

document.getElementById("delet").addEventListener("click", function() {
    let books = JSON.parse(localStorage.getItem("books")) || [];
    books.pop()
    localStorage.setItem("books", JSON.stringify(books));
    location.reload();
});

window.onload = showBooks2;



