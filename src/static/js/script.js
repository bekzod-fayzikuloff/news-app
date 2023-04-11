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


function initDetail() {

    const dislikeBtn = document.querySelector("#dislike")
    const likeBtn = document.querySelector("#like")

    const likes = localStorage.getItem("likes")
    const dislikes = localStorage.getItem("dislikes")

    if (likes && likes.includes(window.location.pathname)) {
        likeBtn.classList.add("liked")
    } if (dislikes && dislikes.includes(window.location.pathname)) {
        dislikeBtn.classList.add("disliked")
    }

    dislikeBtn.addEventListener('click', () => {
        const dislikes = JSON.parse(localStorage.getItem('dislikes'))
        if (dislikes && dislikes.includes(window.location.pathname)) {
            localStorage.removeItem("dislikes")
            localStorage.setItem("dislikes", JSON.stringify(dislikes.filter(dislike => dislike !== window.location.pathname)))
            dislikeBtn.classList.remove("disliked")
            return
        }
        localStorage.setItem('dislikes', JSON.stringify([window.location.pathname]))
        dislikeBtn.classList.add("disliked")
    })
    likeBtn.addEventListener('click', () => {
        const likes = JSON.parse(localStorage.getItem('likes'))
        if (likes && likes.includes(window.location.pathname)) {
            localStorage.removeItem("likes")
            localStorage.setItem("likes", JSON.stringify(likes.filter(likes => likes !== window.location.pathname)))
            likeBtn.classList.remove("liked")
            return
        }
        localStorage.setItem('likes', JSON.stringify([window.location.pathname]))
        likeBtn.classList.add("liked")
    })

}

(async function initScript() {
    if (window.location.pathname === "/news/") {
        await initNewsRender("http://127.0.0.1:8000/api/news/")
    } else if (/[0-9]/.test(window.location.pathname)) {
        initDetail()
    } else {
        const splitPath = window.location.pathname.split("/")
        await initNewsRender(`http://127.0.0.1:8000/api/news/tags/${splitPath[splitPath.length - 2]}/`)
    }
})()
