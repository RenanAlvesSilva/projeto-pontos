$(".btn-close").click(()=>{
    $(".navegation").fadeOut()
    $(".menu-show").removeClass("d-none")
    $(".cards-manager").css("grid-template-columns","'0fr' '1fr'" )
})

$("#menu-showing").click(()=>{
    $(".navegation").fadeIn()
    $(".menu-show").addClass("d-none")
})
