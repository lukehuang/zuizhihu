function addPrefix(group) {
    group.each(function() {
        var src;
        
        if ($(this).attr("src").substring(0, 6) != "https:") {
            src = "http:" + $(this).attr("src");
        } else {
            src = "http:" + $(this).attr("src").substring(6);
        }

        $(this).attr("src", src);
    });
}

$(document).ready(function() {
    // add prefix http: to image sources
    addPrefix($("img"));
});