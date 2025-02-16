localStorage.clear();

class Book {
    constructor(title, authore, desc, read){
        this.title = title;
        this.authore = authore;
        this.desc = desc;
        this.read = read;
    }

    Save (){
        const books = JSON.parse(localStorage.getItem("books")) || [];
    
        books.push(this);

        localStorage.setItem("books", JSON.stringify(books));

        // if (!books.some(book => book.title === this.title)) {
        //     books.push(this);
        //     localStorage.setItem("books", JSON.stringify(books));
        // }
    }

    static getA(){
        return JSON.parse(localStorage.getItem("books")) || [];
    }

    static deletBtn (title){
        let books = JSON.parse(localStorage.getItem("books")) || [];
        books = books.filter(book => book.title !== title);
        localStorage.setItem("books", JSON.stringify(books));
    }
}


function showBooks () {
    
    const books = Book.getA();
    const shelf = document.getElementById("shelf");
    shelf.innerHTML = "";

    books.forEach(book => {
       const bkdiv = document.createElement("div");
       bkdiv.classList.add("bkdiv") //this is class to stile 

       const forTitle = document.createElement("h2");
       forTitle.textContent = book.title;

       const authore = document.createElement("h3");
       authore.textContent = book.authore;

       const descript = document.createElement("p");
       descript.textContent = book.desc;

       const read = document.createElement("p");
       read.textContent = `status: ${book.read}`; 

       //

       bkdiv.appendChild(forTitle);
       bkdiv.appendChild(authore);
       bkdiv.appendChild(descript);
       bkdiv.appendChild(read);

       shelf.appendChild(bkdiv);
    });
}




const test3 = new Book("title 1", "author 1", "good book", true);
const test4 = new Book("title 2", "author 2", "good book", false);
const test5 = new Book("title 3", "author 2", "good book", false);
test3.Save();
test4.Save();
test5.Save();
window.onload = showBooks;
