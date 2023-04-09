const renderPost = (post) => {
    /*Фунция отрисовки новости*/
    const container = document.createElement('div');
    container.className = "card"
    container.innerHTML = `
    <div class="card-body">
    <img src="${post.image}" class="card-img-top" alt="...">
        <h5 class="card-title">${post.title}</h5>
        <p class="card-text">${post.text}</p>
        <a href="http://127.0.0.1:8000/news/${post.id}" class="btn btn-primary">Подробнее</a>
    </div>
    `;
    document.querySelector('#root').appendChild(container);
}

async function initNewsRender(rootUrl) {
    // let url = "http://127.0.0.1:8000/api/news/"

    let renderPosts;
    const loadChuck = async (url) => {
        let response = await fetch(url);
        if (response.status === 200) {
            return await response.json()
        }
    }

    let {next, results} = await loadChuck(rootUrl)
    renderPosts = [...results]

    while (renderPosts.length < 3 && !!next) {
        const data = await loadChuck(next)
        next = data.next
        renderPosts = [...renderPosts, ...data.results]
    }
    renderPosts.map(p => renderPost(p))

    window.addEventListener("scroll", async () => {
        const scrollableHeight = document.documentElement.scrollHeight - window.innerHeight
        if (window.scrollY >= scrollableHeight) {
            if (!!next) {
                let response = await loadChuck(next)
                next = response.next
                response.results.map(p => renderPost(p))
            }
        }
    })
}

(async function initScript() {
    if (window.location.pathname === "/news/") {
       await initNewsRender("http://127.0.0.1:8000/api/news/")
    } else if (/[0-9]/.test(window.location.pathname)){
        console.log("Detail page")
    } else {
        const splitPath = window.location.pathname.split("/")
        await initNewsRender(`http://127.0.0.1:8000/api/news/tags/${splitPath[splitPath.length - 2]}/`)
    }
})()
