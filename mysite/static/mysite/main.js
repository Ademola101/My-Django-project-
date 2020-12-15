$(document).ready(function(){
    var maxLenght = 50;
$(".show-read-more").each(function(){
    var myStr = $(this).text();
    if($.trim(myStr).length > maxLenght){
        var newStr = myStr.substring(0, maxLenght);
        var removedStr = myStr.substring(maxLenght,$.trim(myStr).length);
        $(this).empty().html(newStr);
        $(this).append('<a href ="javascript:void(0);" class = "read-more"> read more...</a>');
        $(this).append('<span class = "more-text">' + removedStr + '</span>');
}

});$(".read-more").click(function(){
    $(this).siblings(".more-text").contents().unwrap();
    $(this).remove();
});});

$(document).ready(function(){
    var showChar = 50
    var ellipsetext ="...";
    var moretext = "Show more >";
    var lesstext = "Show less";

    $("more").each(function(){
        var content = $(this).html();
        if(content.length > showChar){
            var c = content.substr(0, showChar);
            var h = content.substr(showChar, content.length - showChar);
            var html = c + 'span class="moreellipses">' +ellipsetext+'&nbsp;</span><span class ="morecontent"><span>' + h + '</span>&nbsp;&nbsp;<a href="" class="morelink">' + moretext + '</a></span>';
            $(this).html(html);}
        });
        $(".morelink").click(function(){
            if($(this).hasClass("less")){
                $(this).removeClass("less");
                $(this).html(moretext);
            }else {
                $(this).addClass("less");
                $(this).html(lesstext);
            }
            $(this).parent().prev().toggle();
            $(this).prev().toggle();
            return false;
        });

        
    });
    
class_name = getElementsByClassName("nav-item")
console.log(class_name);