async function loadAuthors() {
    const res = await fetch("/products/all-authors/")
    const data = await res.json()
    console.log(data)
    data.forEach(author => {
        const option = document.createElement("option")
        option.textContent = author.name
        option.setAttribute("value", author.id)
        const selectEl = document.querySelector("#author")
        selectEl.appendChild(option)
    });
}

async function loadDates() {
    const res = await fetch("/products/dates/")
    const data = await res.json()
    console.log(data)
    data.forEach(date => {
        const option = document.createElement("option")
        option.textContent = date
        option.setAttribute("value", date)
        const selectEl = document.querySelector("#date")
        selectEl.appendChild(option)
    });
}

loadAuthors()
loadDates()