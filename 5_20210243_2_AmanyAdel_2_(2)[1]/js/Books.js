let books = [];
if (localStorage.getItem("books") != null) {
  books = JSON.parse(localStorage.getItem("books"));
} else {
  books = [
    {
      id: 1,
      author: "Harper Lee",
      name: "To Kill a Mockingbird",
      category: "Fiction",
      description:
        "A classic novel set in the American South during the 1930s.",
    },
    {
      id: 2,
      author: "George Orwell",
      name: "1984",
      category: "Dystopian Fiction",
      description:
        "A dystopian novel set in a totalitarian society, where the government monitors and controls every aspect of human life.",
    },
    {
      id: 3,
      author: "F. Scott Fitzgerald",
      name: "The Great Gatsby",
      category: "Classic Literature",
      description:
        "A novel set in the Roaring Twenties, exploring themes of wealth, love, and the American Dream.",
    },
    {
      id: 4,
      author: "Jane Austen",
      name: "Pride and Prejudice",
      category: "Romance",
      description:
        "A romantic novel set in rural England, revolving around the lives of the Bennet sisters and their romantic pursuits.",
    },
    {
      id: 5,
      author: "J.D. Salinger",
      name: "The Catcher in the Rye",
      category: "Coming-of-Age Fiction",
      description:
        "A coming-of-age novel narrated by Holden Caulfield, a disillusioned teenager navigating the complexities of adolescence and adulthood.",
    },
    {
      id: 6,
      author: "J.K. Rowling",
      name: "Harry Potter and the Sorcerer's Stone",
      category: "Fantasy",
      description:
        "The first book in the Harry Potter series, following the journey of a young wizard named Harry Potter as he discovers his magical heritage and attends Hogwarts School of Witchcraft and Wizardry.",
    },
    {
      id: 7,
      author: "J.R.R. Tolkien",
      name: "The Lord of the Rings",
      category: "Fantasy",
      description:
        "An epic high-fantasy novel set in the fictional world of Middle-earth, following the quest to destroy the One Ring and defeat the Dark Lord Sauron.",
    },
    {
      id: 8,
      author: "Herman Melville",
      name: "Moby-Dick",
      category: "Adventure",
      description:
        "A novel that tells the story of Ishmael's voyage aboard the whaling ship Pequod, led by the obsessed Captain Ahab in pursuit of the legendary white whale, Moby Dick.",
    },
    {
      id: 9,
      author: "Leo Tolstoy",
      name: "War and Peace",
      category: "Historical Fiction",
      description:
        "An epic novel set against the backdrop of Napoleonic Wars, depicting the lives of Russian aristocrats and their struggles for survival and love.",
    },
    {
      id: 10,
      author: "Mark Twain",
      name: "The Adventures of Huckleberry Finn",
      category: "Adventure",
      description:
        "A novel narrated by Huck Finn, a young boy who embarks on a journey down the Mississippi River with an escaped slave named Jim, exploring themes of race, identity, and freedom.",
    },
    {
      id: 11,
      author: "Miguel de Cervantes",
      name: "Don Quixote",
      category: "Satire",
      description:
        "A satirical novel that follows the adventures of Alonso Quixano, who becomes convinced that he is a knight-errant named Don Quixote, and his loyal squire Sancho Panza.",
    },
    {
      id: 12,
      author: "Fyodor Dostoevsky",
      name: "The Brothers Karamazov",
      category: "Philosophical Fiction",
      description:
        "A philosophical novel that explores themes of morality, faith, and free will through the lives of the Karamazov brothers: Dmitri, Ivan, and Alyosha.",
    },
    {
      id: 13,
      author: "Alexandre Dumas",
      name: "The Count of Monte Cristo",
      category: "Adventure",
      description:
        "A tale of revenge and redemption, following the journey of Edmond Dantès, a young sailor who is wrongfully imprisoned and seeks vengeance against those who betrayed him.",
    },
    {
      id: 14,
      author: "Gabriel García Márquez",
      name: "One Hundred Years of Solitude",
      category: "Magical Realism",
      description:
        "A landmark novel that chronicles the multi-generational saga of the Buendía family in the fictional town of Macondo, blending elements of fantasy, myth, and history.",
    },
    {
      id: 15,
      author: "Leo Tolstoy",
      name: "Anna Karenina",
      category: "Romance",
      description:
        "A tragic love story that follows the affair between the married Anna Karenina and the affluent Count Vronsky, set against the backdrop of Russian high society.",
    },
    {
      id: 16,
      author: "Oscar Wilde",
      name: "The Picture of Dorian Gray",
      category: "Gothic Fiction",
      description:
        "A Gothic novel that explores the consequences of vanity and decadence, following the life of Dorian Gray, a young man who remains youthful while a portrait of him ages.",
    },
    {
      id: 17,
      author: "Charles Dickens",
      name: "A Tale of Two Cities",
      category: "Historical Fiction",
      description:
        "A historical novel set in London and Paris before and during the French Revolution, exploring themes of sacrifice, resurrection, and the struggle for justice.",
    },
    {
      id: 18,
      author: "Fyodor Dostoevsky",
      name: "Crime and Punishment",
      category: "Psychological Thriller",
      description:
        "A psychological thriller that follows the story of Rodion Raskolnikov, a young student who commits a murder and grapples with the moral and psychological consequences of his actions.",
    },
    {
      id: 19,
      author: "Emily Brontë",
      name: "Wuthering Heights",
      category: "Gothic Fiction",
      description:
        "A Gothic novel that tells the story of the passionate and destructive love between Catherine Earnshaw and Heathcliff, spanning generations and set on the Yorkshire moors.",
    },
    {
      id: 20,
      author: "Mary Shelley",
      name: "Frankenstein",
      category: "Gothic Fiction",
      description:
        "A Gothic novel that explores themes of scientific hubris and existentialism, following the ambitious scientist Victor Frankenstein and his creation, the Creature.",
    },
    {
      id: 21,
      author: "J.R.R. Tolkien",
      name: "The Hobbit",
      category: "Fantasy",
      description:
        "A fantasy novel about the journey of the hobbit Bilbo Baggins as he embarks on an epic quest to reclaim the Lonely Mountain and its treasure from the dragon Smaug.",
    },
    {
      id: 22,
      author: "Dante Alighieri",
      name: "The Divine Comedy",
      category: "Epic Poetry",
      description:
        "An epic poem that follows the journey of the narrator through Hell, Purgatory, and Paradise, guided by the Roman poet Virgil and his beloved Beatrice.",
    },
    {
      id: 23,
      author: "Homer",
      name: "The Odyssey",
      category: "Epic Poetry",
      description:
        "An epic poem attributed to the ancient Greek poet Homer, recounting the adventures of the hero Odysseus as he tries to return home to Ithaca after the Trojan War.",
    },
    {
      id: 24,
      author: "Arthur Conan Doyle",
      name: "The Adventures of Sherlock Holmes",
      category: "Mystery",
      description:
        "A collection of detective stories featuring the renowned detective Sherlock Holmes and his loyal companion Dr. John Watson, solving mysteries and catching criminals in Victorian London.",
    },
    {
      id: 25,
      author: "Victor Hugo",
      name: "Les Misérables",
      category: "Historical Fiction",
      description:
        "A historical novel set in early 19th-century France, following the lives of several characters, including the ex-convict Jean Valjean, as they struggle for redemption and justice.",
    },
    {
      id: 26,
      author: "Charlotte Brontë",
      name: "Jane Eyre",
      category: "Gothic Fiction",
      description:
        "A Gothic novel that follows the life of Jane Eyre, an orphaned governess, as she faces numerous challenges and finds love at Thornfield Hall, the estate of the mysterious Mr. Rochester.",
    },
    {
      id: 27,
      author: "Bram Stoker",
      name: "Dracula",
      category: "Gothic Fiction",
      description:
        "A Gothic horror novel that introduces the iconic vampire Count Dracula, who terrorizes the people of England and seeks to spread his undead curse.",
    },
    {
      id: 28,
      author: "Charles Dickens",
      name: "Great Expectations",
      category: "Classic Literature",
      description:
        "A bildungsroman novel that follows the life of the orphan Pip, tracing his journey from childhood to adulthood as he aspires to become a gentleman and win the heart of the cold-hearted Estella.",
    },
    {
      id: 29,
      author: "Homer",
      name: "The Iliad",
      category: "Epic Poetry",
      description:
        "An ancient Greek epic poem attributed to Homer, recounting the events of the Trojan War, focusing on the rage of Achilles and the heroism of other Greek and Trojan warriors.",
    },
    {
      id: 30,
      author: "Oscar Wilde",
      name: "The Picture of Dorian Gray",
      category: "Gothic Fiction",
      description:
        "A Gothic novel that tells the story of Dorian Gray, a young man whose portrait ages while he remains eternally youthful, as he descends into corruption and depravity.",
    },
    {
      id: 31,
      author: "Robert Louis Stevenson",
      name: "Treasure Island",
      category: "Adventure",
      description:
        "An adventure novel that follows the quest for buried treasure by the young Jim Hawkins, the pirate Long John Silver, and their crew, aboard the Hispaniola.",
    },
    {
      id: 32,
      author: "Alexandre Dumas",
      name: "The Three Musketeers",
      category: "Historical Fiction",
      description:
        "A historical adventure novel set in 17th-century France, following the adventures of d'Artagnan, a young nobleman, and the Three Musketeers: Athos, Porthos, and Aramis.",
    },
    {
      id: 33,
      author: "Lewis Carroll",
      name: "Alice's Adventures in Wonderland",
      category: "Fantasy",
      description:
        "A fantasy novel that follows the adventures of a young girl named Alice as she falls down a rabbit hole into a whimsical world filled with eccentric characters and nonsensical events.",
    },
    {
      id: 34,
      author: "Margaret Mitchell",
      name: "Gone with the Wind",
      category: "Historical Fiction",
      description:
        "A historical novel set in the American South during the Civil War and Reconstruction era, following the life of Scarlett O'Hara, a headstrong Southern belle, and her romantic entanglements with Rhett Butler.",
    },
    {
      id: 35,
      author: "Charles Dickens",
      name: "Oliver Twist",
      category: "Social Novel",
      description:
        "A social novel that depicts the harsh realities of life for orphaned children in Victorian London, following the adventures of the young orphan Oliver Twist.",
    },
    {
      id: 36,
      author: "Jules Verne",
      name: "Twenty Thousand Leagues Under the Sea",
      category: "Adventure",
      description:
        "An adventure novel that follows the journey of Captain Nemo and the crew of the submarine Nautilus as they explore the depths of the ocean and encounter various marine creatures.",
    },
    {
      id: 37,
      author: "Jane Austen",
      name: "Sense and Sensibility",
      category: "Romance",
      description:
        "A romantic novel that follows the romantic pursuits of the Dashwood sisters, Elinor and Marianne, as they navigate love, heartbreak, and societal expectations in Regency England.",
    },
    {
      id: 38,
      author: "Ernest Hemingway",
      name: "The Old Man and the Sea",
      category: "Novella",
      description:
        "A novella that tells the story of an aging Cuban fisherman named Santiago and his epic battle to catch a giant marlin in the Gulf Stream.",
    },
    {
      id: 39,
      author: "F. Scott Fitzgerald",
      name: "Tender Is the Night",
      category: "Modernist Literature",
      description:
        "A modernist novel that follows the lives of Dick and Nicole Diver, a glamorous couple living on the French Riviera, as their marriage unravels amidst personal and social upheaval.",
    },
    {
      id: 40,
      author: "H.G. Wells",
      name: "The War of the Worlds",
      category: "Science Fiction",
      description:
        "A science fiction novel that depicts an invasion of Earth by Martians, exploring themes of imperialism, warfare, and the resilience of humanity.",
    },
  ];

}
let BTable = document.getElementById("booksTable");
function displayBooks(arr) {
  var temp = ``;
  for (let i = 0; i < arr.length; i++) {
    temp += `<tr>
    <td>${i + 1}</td>
    <td>${arr[i].id}</td>
    <td>${arr[i].author}</td>
    <td>${arr[i].name}</td>
    <td>${arr[i].category}</td>
    <td>${arr[i].description}</td>
    <td>
  <button class="borrow-button">Borrow </button>
    </td>
    </tr>`;
  }
  BTable.innerHTML = temp;
}
displayBooks(books);