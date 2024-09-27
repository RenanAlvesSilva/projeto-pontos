$("#btn-close").click(()=>{
    $(".navegation").fadeOut()
    $(".menu-show").removeClass("d-none")
    
    $("header").css("width", "0px")
    $("#my-grid").css("grid-template-columns", " '0fr' '4fr' ")
    
})

$("#menu-showing").click(()=>{
    $(".navegation").fadeIn()
    $(".menu-show").addClass("d-none")
    $("#sidebar").css("height", "100vh")
    $("#my-grid").css("grid-template-columns", " '1fr' '4fr' ")
    $("header").css("width", "300px")
    
})
