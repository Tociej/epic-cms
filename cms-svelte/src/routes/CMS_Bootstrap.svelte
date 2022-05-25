<script>
    let article_id;
    let slides = [], news = [], articles = [], features = [], slide_interval, order = [];
    // let slides = [
    //     {content: "first slide", header: "ONE SLIDE", bg: "https://wally.com.pl/galerie/t/tapeta-na-sciane-gory-032_55845.jpg", fg: "white"},
    //     {content: "2nd slide", bg: "https://www.imperiumtapet.com/public/uploads/preview/krajobraz-20421535474510e55t5qdn5p.jpg", fg: "yellow"},
    //     {content: "3", bg: "https://th.bing.com/th/id/R.c14ec6e89a110fa4756127ff14c0d658?rik=%2f%2bZfVI%2fTZqJN6Q&pid=ImgRaw&r=0", fg: "black"},
    //   ]

    // let news = [
    //     {content: "new products omg", header: "head", address:"1"},
    //     {content: "good news everyone!", address:"2"},
    //     {content: "poland mountain", address:"3"},
    //     {content: "new4", address: "4"},
    //     {content: "new5", address: "5"}
    // ]

    // let features = [
    //     {content: "This is first feature", header: "great feature", imgsrc: "https://i.imgur.com/WpE9bNBb.jpg"},
    //     {content: "This is really nice feautere", header: "great one really", imgsrc: "https://i.imgur.com/WpE9bNBb.jpg"}
    // ]
    let temp
    let slidesheight = "500px";
    let newscolumns = 3;

    //let order = ["slider", "news" ,"features"]

    let page = "home";
    //will change it on log in
    let isLoggedIn = false;
    let login, password, perms;
    let settingspage = 0;

    let text_color, background_color, border_color, header_background_color, header_text_color, font_family, font_size;
    let connected = 0;
    //fetch data from api
    async function getData() {
      let result;
      let response = await fetch("http://localhost:5000/getData", {method: "post"})
                    .then(res => res.json()).then(data => result = data) ;
      
      features = result.features
      slides = result.slider.slides
      news = result.news
      slide_interval = result.slider.speed
      order = result.settings.order
      text_color = result.settings.color;
      background_color = result.settings.bgcolor;
      border_color = result.settings.border;
      header_background_color = result.header.bgcolor;
      header_text_color = result.header.color;
      font_family = result.settings.fontfamily;
      font_size = result.settings.fontsize;
      console.log(news)
      
      connected = 1

      return result;
    
    }

    async function updateContents(){
      let bruh;
        await fetch('http://localhost:5000/setData', {
          method: 'POST', // or 'PUT'
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({slider: {slides: slides, speed: slide_interval }, news: news, features: features, settings: {color: text_color, bgcolor: background_color, border: border_color, fontfamily: font_family, fontsize: font_size, order: order }, header: {color: header_text_color, bgcolor: header_background_color}}),
        }).then(res => res.json()).then(data => bruh = data)
        if(bruh.res == "work") {
          console.log("work")
        } else {
          console.log("bad")
        }
    }
  

    function changeOrder(pos, item){
      order.splice(pos, 1)
      item = [item]
      order = item.concat(order)
    }

    function deleteSlide(id){
      slides.splice(id, 1)
      slides = slides
    }

    function deleteNews(id){
      news.splice(id,1)
      news = news
    }
    function deleteFeatures(id){
      features.splice(id,1)
      features = features
    }
    function ඞ(){
      console.log("amogus")
    }

    function logout() {
      login = null;
      isLoggedIn = false;
      perms = null;
      password = null;
      page = "home";
    }

    async function loginto(){
      let result;
      await fetch('http://localhost:5000/login', {
          method: 'POST', headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({user: login, password: password}),
        }).then(res => res.json()).then(data => result = data)
        console.log(result)
      if(result.res == "pog") {
        login = result.user;
        perms = result.perms
        isLoggedIn = true;
        page = "home"
      } else {
        console.log(`bad: ${result.res}`)
      }
      
      
    }
    async function register(){
      await fetch('http://localhost:5000/register', {
          method: 'POST', // or 'PUT'
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({user: user, password: pass}),
        }).then(response => response.json).then(data => res = data)
        
      if(res.res =="pog") {
        isLoggedIn = true;
        page = "home"
        login = res.user;
        perms = res.perms
      } else {
        console.log("bad nickname or pass or server err i dunno")
        console.log("rip bozo ඞ")  /* 
        bozo
        /ˈbəʊzəʊ/
        noun: bozo; plural noun: bozos
         a stupid or insignificant man.*/
      }
      
      
    }
   

    async function postComment() {

      if(temp == " ") {
        // fix it
        return
      }
      await fetch('http://localhost:5000/postComment', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({articleid: article_id, user: login, comment: temp})
      }).then(res => res.json()).then(data => news[article_id].comments = data)
      temp = "";

    }
    
    async function deleteComment(id) {
      await fetch('http://localhost:5000/deleteComment', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({articleid: article_id, id: id})
      }).then(res => res.json()).then(data => news[article_id].comments = data)
    }
    
    getData()//dontchu say?


</script>
  
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="ඞ">
    <meta name="author" content="ඞ">


    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>


    <style>
      :root{
        --border-color: #4b5563;
        --text-color: black;
        --background-color: white;
        --header-background-color: grey;
        --header-text-color: black;
        height: 100%;
      }
      html{
        background-color: var(--background-color);

      }
      body{
        padding: 0;
        color: inherit;
        background-color: var(--background-color);
        border: none;
        height: 100%;
        margin: 0;
        top:0;
        

      }
      .navbar{
        background-color: var(--header-background-color);
      }
      nav a, .nav-item a{
        color: var(--header-text-color);
      }
      .settingsmain input{
        background-color: var(--background-color);
      }
      /* .btn{
        border: 1px solid var(--border-color);
        color: var(--border-color);
        background-color: var(--background-color);
      } */
      .settingscategories{
        margin-left: 10px;
        margin-right: 10px;
        margin-top: 1px;
      }
      .settingscategories div{
        border: none;
      }
      .activecat{
        border: 1px solid var(--border-color)!important;
      }

      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
      }
      input, button{
        border: 1px solid var(--border-color);
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
      .loginbox{
        border: 1px solid var(--border-color);
      }
      .motive{
        text-align: center;
      }
    </style>
    
</head>
{#if connected == 0}
  <p>*imagine a cool loading screen*</p>
   <button class="btn" on:click={() => getData()}>refresh</button> <!-- XDDDDDDDDDDDDDDDDDDDD -->
{/if}
{#if connected == 1}



<body style="--text-color: {text_color}; color: var(--text-color);
            --border-color: {border_color}; border-color: var(--border-color);
            --background-color: {background_color}; background-color: var(--background-color);
            font-family: {font_family}">

            <header>

              <nav class="navbar navbar-expand-md fixed-top"
                   style="--header-background-color: {header_background_color}; background-color: var(--header-background-color);
                          --header-text-color: {header_text_color}; color: var(--header-text-color)">
                <div class="container-fluid">
                  <a class="navbar-brand" href="#" on:click={() => {page = "home"}}>Home</a>
                  <button class="navbar-toggler" style="stroke: var(--header-text-color); background: none;" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon" style="stroke: var(--header-text-color); bakground: none;"></span>
                  </button>
                  <div class="collapse navbar-collapse" id="navbarCollapse">
                    <ul class="navbar-nav me-auto mb-2 mb-md-0">
                      <li class="nav-item">
                        <a class="nav-link" href="#" on:click={()=>(page="articles")}>Articles</a>
                      </li>
            
                      {#if isLoggedIn && perms == 1} 
                      <li class="nav-item">
                        <a class="nav-link" href="#" on:click={(()=>(page = "settings"))}>Settings</a>
                      </li>
                      {/if}
            
            
                      <!-- <li class="nav-item"> 
                        <a class="nav-link disabled">Disabled</a>
                      </li> -->
                    </ul>
                    {#if isLoggedIn}
                     <form class="d-flex">
                      <b class="text-center">Hello {login}</b>
                      <button class="btn btn-secondary" on:click={(() => logout())}>Logout</button>
                     </form> 
                    {/if}
                    <form class="d-flex">
            
                    <!-- funky buttons-->      
                      {#if !isLoggedIn}
                      <button class="btn btn-outline-success" on:click={() => (page = "login")}>Login</button>
                      <button class="btn btn-outline-primary ml-3" on:click={() => (page = "login")}>Register</button>
                      {/if}
                    </form>
                  </div>
                </div>
              </nav>
            </header>

{#if page === "home"}
  


<main style="margin-top: 55px; background: inherit;">
  {#each order as item, itemid}
    {#if item == "slider"}
  <div id="myCarousel" class="carousel slide" data-bs-ride="carousel" data-bs-interval="{slide_interval}">
    <div class="carousel-indicators">
      {#each slides as slide, id}
      <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="{id}" class="{(0 == id? "active" : " ")}" aria-current="{(0 == id? "true" : "false")}" aria-label="Slide {id}"></button>
      {/each}  
    </div>
    <div class="carousel-inner">

      {#each slides as slide, id}
      <!-- item -->
      <div class="carousel-item {id == 0 ? " active" : ""}">
        <img class="bd-placeholder-img" src="{slide.bg}" width="100%" alt="no link provided" style="max-height: {slidesheight}">

        <div class="container">
          <div class="carousel-caption text-start" style="color: {slide.fg};">
            <h1>{slide.header != undefined ? slide.header : " "}</h1>
            <p>{slide.content}</p>
            <p><button class="btn sliderbutton" style="background: none; border: 1px solid {slide.fg}; color: {slide.fg};">Check it out!</button></p>
          </div>
        </div>
      </div>
      {/each}
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#myCarousel" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#myCarousel" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
  {/if}

  {#if item === "news"}
  <div class="container marketing">
    <div class="row">
      {#each news as article, id}
        <div class="col m-1" style="border: 2px solid var(--border-color);">
          <h2>{article.header}</h2>
          <p>{article.content}</p>
          <p><button class="btn" style="background-color: var(--border-color); color: var(--background-color);" on:click={()=>(page = "articles", article_id = id)}>View details &raquo;</button></p>
        </div>
        {#if (id + 1) % newscolumns == 0}<div class="w-100"></div>{/if}
      {/each}
    </div>
  </div>
  {/if}

  {#if item === "features"}
  <div class="container marketing">
    <!-- START THE FEATURETTES -->
    
      <hr class="featurette-divider">

      {#each features as feature, id}
      <div class="row featurette">
        <div class="col-md-7 {id %2 == 0 ? "order-md-2 text-end" : ""}">
          <h2 class="featurette-heading">{feature.header}<span class="text-muted"><!-- funky text --></span></h2>
          <p class="lead">{feature.content}</p>
        </div>
        <div class="col-md-5 {id %2 == 0 ? "order-md-1" : ""}">
          <img class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto" alt="no link provided" width="500" height="500" src="{feature.imgsrc}"/>
        </div>
      </div>

      <hr class="featurette-divider">
      {/each}

      <!-- /END THE FEATURETTES -->
    
  </div><!-- /.container -->
  {/if}

  <!-- FOOTER -->

  {/each}
  <footer class="container">
    <p class="float-end"><a href="#">Back to top</a></p>
    <p>Authors: Paweł Augustyn, Maciej Tokarz</p>
  </footer>
</main>
{/if}

{#if page === "login"}

  <form class="loginbox mx-auto p-5 rounded w-50 row align-middle mt-5" style="margin-top: 55px; color: black !important">
    <div class="col">
      Login:
    </div>
    <input class="col rounded" bind:value={login}>
    
    <div class="w-full my-1"></div>

    <div class="col">
      Password:
    </div>
    <input class="col rounded" style="color: black !important" bind:value={password}>

    <div class="w-full my-1" style="color: black !important"></div>

    <button class="col rounded" on:click={(()=>(loginto()))}>Login</button>
    <button class="col rounded" on:click={(()=>(register()))}>Register</button>
  </form>


{/if}

{#if page === "article"}
{#key news}
<main style="margin-top: 55px;" class="p-3">
  
  <h2>{news[article_id].header}</h2>
  <div>
    {news[article_id].article}
  </div>
  <div class="comments rounded row p-3" style="border-width: 5px; border-color: var(--border-color);">
    {#each news[article_id].comments as comment, id}
      <p class="col">{comment.user} : {comment.text}</p>
      {#if comment.user == login || perms > 0 && isLoggedIn}
        <button class="col" on:click={()=> (deleteComment(id))}>delete</button>
      {/if}
      <hr class="my-1">
      <div class="w-100"></div>
    {/each}

    {#if isLoggedIn}
    <input class="col" type="text" style="color: black !important" bind:value={temp}>
    <div class="col"></div>
    <button class="col" on:click={()=>(postComment())}>submit</button>
    {/if}
  </div>
</main>
{/key}
{/if}

{#if page === "articles"}
<!-- filtering lol -->
<div class="container marketing" style="margin-top: 55px;">
  <div class="row">
    {#each news as article, id}
      <div class="col m-1" style="border: 2px solid var(--border-color);">
        <h2>{article.header}</h2>
        <p>{article.content}</p>
        <p><button class="btn" style="background-color: var(--border-color); color: var(--background-color);" on:click={()=>(page = "article", article_id = id)}>View details &raquo;</button></p>
      </div>
      {#if (id + 1) % newscolumns == 0}<div class="w-100"></div>{/if}
    {/each}
  </div>
</div>
{/if}

{#if page === "settings"}
  <nav class="navbar nav" style="--header-background-color: {header_background_color}; background-color: var(--header-background-color);
  --header-text-color: {header_text_color}; color: var(--header-text-color); margin-top: 60px;">
      <div class="row settingscategories w-100">
        <div class="col {(settingspage == 0 ? "activecat" : "")}" on:click={() => (settingspage = 0)}>Colors & Order</div>
        <div class="col {(settingspage == 1 ? "activecat" : "")}" on:click={() => (settingspage = 1)}>Menu główne</div>
        <div class="col {(settingspage == 2 ? "activecat" : "")}" on:click={() => (settingspage = 2)}>Slider</div>
        <div class="col {(settingspage == 3 ? "activecat" : "")}" on:click={() => (settingspage = 3)}>News</div>
        <div class="col {(settingspage == 5 ? "activecat" : "")}" on:click={() => (settingspage = 5)}>Features</div>
      </div>
  </nav>
  <div class="mx-5 my-1 rounded settingsmain" style="border: 1px solid var(--border-color);">
    <div class="row p-4">
      {#if settingspage === 0}
      
        <div class="col">Text Color:</div> <input class="col" type="color" bind:value={text_color} placeholder={text_color}>
        <div class="w-full"></div>
        <div class="col">Background Color:</div> <input class="col" type="color" bind:value={background_color}>
        <div class="w-full"></div>
        <div class="col">Border Color:</div> <input class="col" type="color" bind:value={border_color}>
        <div class="w-full"></div>
        <div class="col">Font Family</div> <input class="col" type="text" bind:value={font_family}>
        <div class="w-full"></div>
      
        <div class="col">Elements order: {order}</div>
        <div class="w-full"></div>

        {#each order as item, id}
          <button class="rounded-circle text-center ml-4" style="line-height: 100px; width: 100px; height: 100px; border: 1px solid var(--border-color)" on:click={() => (changeOrder(id, item))}>{item}</button>
          <br>
        {/each}

        <div class="w-full">Motives</div>
        <div class="col motive rounded" style="background-color: white; color: black; border: 2px solid grey;" on:click={() => (text_color = "black", background_color = "white", border_color = "grey", header_background_color = "grey", header_text_color = "black")}>Default</div>
        <div class="col motive rounded" style="background-color: black; color: white; border: 2px solid orange;" on:click={() => (text_color = "white", background_color = "black", border_color = "orange", header_background_color = "black", header_text_color = "orange")}>Dark</div>
        <div class="col motive rounded" style="background-color: green; color: blue; border: 2px solid darkblue;" on:click={() => (text_color = "blue", background_color = "green", border_color = "darkblue", header_background_color = "cyan", header_text_color = "lime")}>Nature</div>
        


      {/if}
      {#if settingspage === 1}

        <div class="w-full"></div>
        <div class="col">Header Text Color: </div> <input class="col" type="color" bind:value={header_text_color}>
        <div class="w-full"></div>
        <div class="col">Header Background Color: </div> <input class="col" type="color" bind:value={header_background_color}>

        <div class="w-full"></div>
        <div class="col">Font Family: </div> <input class="col" type="text" bind:value={font_family}>
        <div class="w-full"></div>
        <div class="col">Font Size: </div> <input class="col" type="text" bind:value={font_size}>

      {/if}

      {#if settingspage === 2}

        <div class="w-full"></div>
        <div class="col">Header</div><div class="col">Content</div><div class="col">Image</div><div class="col">Font Color</div>
       
          {#each slides as slide, id}

            <div class="w-full"></div>

            <input class="col" bind:value={slide["header"]}>
            <input class="col" bind:value={slide["content"]}>
            <input class="col" bind:value={slide["bg"]}>
            <input class="col" bind:value={slide["fg"]}>

            <button class="col" on:click={()=>(deleteSlide(id))}>Delete</button>

          {/each}

              <!-- why dis no work? -->
              <button class="my-1" on:click={()=>(slides = slides.concat({content: "", header: "", bg:"", fg:""}))}>Add empty row</button>

              <div class="w-full"></div>
              <div class="col">Sliders Speed</div><input type="text" bind:value={slide_interval} class="col">

      {/if}      
      
      {#if settingspage == 3}
      
        <div class="w-full"></div>
        <div class="col">Id</div><div class="col">Category</div><div class="col">Header</div><div class="col">Content</div><div class="col">Article</div><div class="col"></div>
          {#each news as newse, id}

            <div class="w-full"></div>
            <div class="col">{id}</div>
            <input class="col" bind:value={newse["category"]}>
            <input class="col" bind:value={newse["header"]}>
            <input class="col" bind:value={newse["content"]}>
            <input class="col" bind:value={newse["article"]}>


            <button class="col" on:click={()=>(deleteNews(id))}>Delete</button>

          {/each}


          <!-- why dis no work? -->
          <button class="my-1" on:click={()=>(news = news.concat({category: "", content: "", header: "", article: "", comments: []}))}>Add empty row</button>  

          <div class="w-full"></div>
          <div class="col">Columns</div> <input class="col" bind:value={newscolumns}>

      {/if}
      {#if settingspage == 5}
      
      <div class="w-full"></div>
      <div class="col">Header</div><div class="col">Content</div><div class="col">Image</div>
        {#each features as feature, id}

          <div class="w-full"></div>

          <input class="col" bind:value={feature["header"]}>
          <input class="col" bind:value={feature["content"]}>
          <input class="col" bind:value={feature["imgsrc"]}>
          <button class="col" on:click={()=>(deleteFeatures(id))}>Delete</button>

        {/each}

            <!-- why dis no work? -->
            <button class="my-1" on:click={()=>(features = features.concat({content: "", header: "", imgsrc:""}))}>Add empty row</button>   

    {/if}


      <div class="w-full"></div>
      <!-- commit changes to server -> database -->
      <button class="w-75 mx-auto my-2" on:click={()=>(page="home", updateContents())}>Confirm</button>

    </div>


    
  </div>

{/if}

</body>

{/if}