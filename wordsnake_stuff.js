$(function(){   
    $('.class').css('float','left');
    $('.answer').after("<div style='clear:both'></div>");

    $('.class').css({border: '2px dashed grey', padding: '10px', margin: '10px 20px', width: '350px'});

    $(".answer").hide();

    $(".answer").before(
        function(){
            var h = $(this).height();
            var w = $(this).width();
            var D = $("<div class='hider' style='float:left; margin:10px; font-size:2em;" + 
                    "padding:10;border:1px solid black'>answer</div>");
            D.css({'height':h, 'width':w});
            return D;
        });
    
    $(".hider").click(function() {
        $(this).slideUp();
        $(this).next('.answer').slideToggle();
        
    });

    $(".censored").click( function() {
        $(this).toggleClass("censored");
    });
        
});
