$(function(){    
    $('.class').css('float','left'); 
    $('.class').css({'margin':'10px 2% 10px 1%','padding':'10px 1%'});
    $('.answer').after("<div style='clear:both'></div>");

    // $('.class').css({border: '2px dashed grey'; padding: '10px', margin: '10px 20px', width: '350px'});
    
    // make a cloned hider div, to get height from clone where needed?
    var D = $("<div class='hider' style='margin:10px; font-size:2em;" +
            "padding:10px;border:1px solid black'>answer</div>");

    // get the height it would take up in flow
    $(D).css({'position':'absolute','visibility':'hidden', 'display':'block'});
    hiderHeight = $(D).height();
    $(D).css({'position':'static','visibility':'visible','display':'none'});

    console.log("H:" + hiderHeight);

    $('.class').css({width: '45%'});
    $(".answer").hide();
    $(".answer").before(
        function(){
            var h = $(this).height();
            var w = $(this).width();
            var D = $("<div class='hider' style='float:left; font-size:2em;" + 
                    "color: lightblue;'>answer</div>");
            $(D).css('visibility','hidden');
            var h1 = $(D).height();
            console.log('h:' + h1 + ":" + h);
            $(D).css({'height':Math.max(h,h1), 'width':"45%"});
            $(D).css('visibility','visible');
            return D;
        }); 
    
    $(".question").before("<hr class='question-hr' style='border: dotted 1px lightblue' />");
    
    $(".hider").click(function() {
        $(this).slideUp();
        $(this).next('.answer').slideDown();
     
    }); 
     
    // $('h1').parent().css('border-bottom','3px solid red')
    var openall = $("<span style='position:fixed; color: lightblue; right:0px; bottom:0px'>(show all answers)</span>").
        click(function() {
            $(".hider").trigger("click");
            $(this).text("(all answers showing)");
        });
    $('body').append(openall);

});

