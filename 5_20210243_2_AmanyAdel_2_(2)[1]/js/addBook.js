let Bid = document.getElementById("bookID");
let BN = document.getElementById("bookN");
let author = document.getElementById("author");
let category = document.getElementById("category");
let desc = document.getElementById("desc");

let storedBooks = JSON.parse(localStorage.getItem("books"));
function addBook() {
  let addedBook = {
    id: Bid.value,
    Author: author.value,
    name: BN.value,
    Category: category.value,
    description: desc.value,
  };
  storedBooks.push(addedBook);
  localStorage.setItem("books", JSON.stringify(storedBooks));
  clearform();
  alert("Added Successfully");
}

function clearform() {
    Bid.value = "";
    BN.value = "";
    author.value = "";
    category.value = "";
    desc.value = "";
}