async function loadAuthors() {
    const res = await fetch("/products/all-authors")
    const data = await res.json()
    data.forEach(author => {
        const option = document.createElement("option")
        option.textContent = author.name
        option.setAttribute("value", author.id)
        const selectEl = document.querySelector("#author")
        selectEl.appendChild(option)
    });
}

loadAuthors()