function addPrefix(group) {
    group.each(function() {
        if ($(this).attr("src").substring(0, 6) != "https:") {
            var src = "https:" + $(this).attr("src");
            $(this).attr("src", src);
        }
    });
}

$(document).ready(function() {
    // add prefix http: to image sources
    addPrefix($("img"));
});